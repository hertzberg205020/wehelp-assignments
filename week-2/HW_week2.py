"""Assignment week2"""
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
    calculate(1, 3)
    calculate(4, 8)
    avg(data)
    print(maxProduct([5, 20, 2, 6]))
    print(maxProduct([10, -2, 0, 3]))
    print(maxProduct([-1, 2]))
    print(maxProduct([-1, 0, 2]))
    print(maxProduct([-1, -2, 0]))
    print(twoSum([2, 11, 7, 15], 9))
    print(maxZeros([0, 1, 0, 0]))
    print(maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]))
    print(maxZeros([1, 1, 1, 1, 1]))
    print(maxZeros([0, 0, 0, 1, 1]))


if __name__ == "__main__":
    main()
