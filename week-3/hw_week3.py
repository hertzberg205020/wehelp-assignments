import csv
import json
import re
from urllib import request


def get_raw_data(src):
    with request.urlopen(src) as response:
        raw_data = response.read().decode("utf-8")
    raw_data = json.loads(raw_data)

    return raw_data['result']['results']


def create_lacation_csv(location_info_lst):
    # sample = location_info_lst[0]
    # print(sample['stitle'])
    # print(sample['longitude'])
    # print(sample['latitude'])
    # print(sample['address'])
    # figsUrl = sample['file'].split("https")
    # print("https" + figsUrl[1])
    temp_lst = [0] * 5
    with open('data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for location in location_info_lst:
            temp_lst[0] = location['stitle']
            address = location['address']
            region = getRegion(address)
            temp_lst[1] = region
            temp_lst[2] = location['longitude']
            temp_lst[3] = location['latitude']
            figsUrl = location['file'].split("https")
            temp_lst[4] = "https" + figsUrl[1]
            writer.writerow(temp_lst)


def getRegion(address):
    """使用正則表達式找出xx區"""
    result = re.search(r".*\s(?P<region>\w{3})", address)
    return result.groupdict()['region']


def main():
    location_info_lst = get_raw_data('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
    create_lacation_csv(location_info_lst)
    # getRegion("臺北市  大同區環河北路一段")


if __name__ == "__main__":
    main()
