"""Assignment week2"""
import heapq
from random import Random
from typing import List


def calculate(min: int, max: int) -> int:
    res = 0
    for num in range(min, max + 1):
        res += num
    print(res)
    return res


data = {"count": 3, "employees": [{'name': 'John', "salary": 30000},
                                  {'name': 'Bob', "salary": 60000},
                                  {'name': 'Jenny', "salary": 50000}]}


def avg(data):
    total = 0
    for employee in data['employees']:
        total += employee['salary']

    res = total / data['count']
    print(res)
    return res


def maxProduct(nums: List):
    mergeSort(nums)
    candidate1 = nums[0] * nums[1]
    candidate2 = nums[-1] * nums[-2]
    return candidate1 if candidate1 >= candidate2 else candidate2


def maxProduct_priority_queue(nums: List):
    # mergeSort(nums)
    largest_items = findKthLargestItems(nums, 2)
    smallest_items = findKthSmallestItems(nums, 2)

    candidate1 = largest_items[0] * largest_items[1]
    candidate2 = smallest_items[0] * smallest_items[1]
    return candidate1 if candidate1 >= candidate2 else candidate2


def maxProduct_partation(nums: List):
    selectK(nums, 2)
    selectK(nums, len(nums)-2 + 1)
    candidate1 = nums[0] * nums[1]
    candidate2 = nums[-1] * nums[-2]
    return candidate1 if candidate1 >= candidate2 else candidate2


def _partation(nums, l, r, rnd):
    p = rnd.randint(0, r-l) + l
    nums[l], nums[p] = nums[p], nums[l]
    # nums[l+1, i-1] <= v; nums[j+1, r] >= v
    i = l + 1
    j = r
    while True:
        while i <= j and nums[i] < nums[l]:
            i += 1
        while i <= j and nums[j] > nums[l]:
            j -= 1
        if i >= j:
            break
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    nums[l], nums[j] = nums[j], nums[l]
    # nums[l, j-1] <= v, nums[j] == v, nums[j+1, r] >= v
    return j


def _selectK(nums, l, r, k, rnd):
    p = _partation(nums, l, r, rnd)
    if p == k:
        return nums[p]
    elif p < k:
        return _selectK(nums, p+1, r, k, rnd)
    else:
        return _selectK(nums, l, p-1, k, rnd)



def selectK(nums: List, k: int):
    rnd = Random()
    return _selectK(nums, 0, len(nums)-1, len(nums)-k, rnd)


def findKthLargestItems(nums: List[int], k: int):
    import heapq
    heap = [nums[i] for i in range(k)]
    heapq.heapify(heap)

    n = len(nums)

    for i in range(k, n):
        if len(heap) != 0 and nums[i] > heap[0]:  # 比最小堆中的最小值還要小
            heapq.heappushpop(heap, nums[i])

    return [item for item in heap]


def findKthSmallestItems(nums: List[int], k: int):
    max_heap = MaxHeap()
    for i in range(k):
        max_heap.heappush(nums[i])

    n = len(nums)

    for i in range(k, n):
        if len(max_heap.h) != 0 and nums[i] < max_heap[0]:
            max_heap.heappop()
            max_heap.heappush(nums[i])
    return [item for item in max_heap]


class MaxHeapObj(object):
  def __init__(self, val): self.val = val
  def __lt__(self, other): return self.val > other.val
  def __eq__(self, other): return self.val == other.val
  def __str__(self): return str(self.val)


class MinHeap(object):
  def __init__(self): self.h = []
  def heappush(self, x): heapq.heappush(self.h, x)
  def heappop(self): return heapq.heappop(self.h)
  def __getitem__(self, i): return self.h[i]
  def __len__(self): return len(self.h)


class MaxHeap(MinHeap):
  def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))
  def heappop(self): return heapq.heappop(self.h).val
  def __getitem__(self, i): return self.h[i].val


def _merge(arr, l, mid, r, temp):
    temp[l:r+1] = arr[l:r+1]
    i = l
    j = mid + 1
    for k in range(l, r+1):
        if i > mid:
            arr[k] = temp[j]
            j += 1
        elif j > r:
            arr[k] = temp[i]
            i += 1
        elif temp[i] <= temp[j]:
            arr[k] = temp[i]
            i += 1
        else:
            arr[k] = temp[j]
            j += 1


def _mergeSort(arr, l, r, temp):
    if l >= r:
        return
    mid = l + (r - l) // 2
    _mergeSort(arr, l, mid, temp)
    _mergeSort(arr, mid + 1, r, temp)
    if arr[mid] > arr[mid+1]:
        _merge(arr, l, mid, r, temp)


def mergeSort(arr: List):
    temp = arr[::]
    _mergeSort(arr, 0, len(arr) - 1, temp)


def maxproduct02(nums: List) -> int:
    """Maximum Product Subarray"""
    max = nums[0]
    cur_subarr_min = nums[0]
    cur_subarr_max = nums[0]

    for i in range(1, len(nums)):
        post_cur_max = cur_subarr_max
        cur_subarr_max *= nums[i]
        if nums[i] > cur_subarr_max:
            cur_subarr_max = nums[i]
        if cur_subarr_min * nums[i] > cur_subarr_max:
            cur_subarr_max = cur_subarr_min * nums[i]
        if cur_subarr_max > max:
            max = cur_subarr_max

        cur_subarr_min *= nums[i]
        if nums[i] < cur_subarr_min:
            cur_subarr_min = nums[i]
        if post_cur_max * nums[i] < cur_subarr_min:
            cur_subarr_min = post_cur_max * nums[i]
    return max



def twoSum(nums: List[int], target: int) -> List[int]:
    res_map = {}
    for num in nums:
        diff = target - num
        if num in res_map:
            return [res_map[num], nums.index(num)]
        else:
            res_map[diff] = nums.index(num)


def maxZeros(nums: List[int]):
    cur_length = 0
    max_length = 0
    for num in nums:
        if num == 0:
            cur_length += 1
        if num == 1:
            if cur_length > max_length:
                max_length = cur_length
            cur_length = 0
    return max_length if max_length > cur_length else cur_length
    

def main():
    """作業測資"""
    # calculate(1, 3)
    # calculate(4, 8)
    # avg(data)
    print(maxProduct([5, 20, 2, 6]))
    print(maxProduct([10, -2, 0, 3]))
    print(maxProduct([-1, 2]))
    print(maxProduct([-1, 0, 2]))
    print(maxProduct([-1, -2, 0]))
    # print(maxProduct_priority_queue([5, 20, 2, 6]))
    # print(maxProduct_priority_queue([10, -2, 0, 3]))
    # print(maxProduct_priority_queue([-1, 2]))
    # print(maxProduct_priority_queue([-1, 0, 2]))
    # print(maxProduct_priority_queue([-1, -2, 0]))
    print(maxProduct_partation([5, 20, 2, 6]))
    print(maxProduct_partation([10, -2, 0, 3]))
    print(maxProduct_partation([-1, 2]))
    print(maxProduct_partation([-1, 0, 2]))
    print(maxProduct_partation([-1, -2, 0]))
    # print(twoSum([2, 11, 7, 15], 9))
    # print(maxZeros([0, 1, 0, 0]))
    # print(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]))
    # print(maxZeros([1, 1, 1, 1, 1]))
    # print(maxZeros([0, 0, 0, 1, 1]))


if __name__ == "__main__":
    main()
