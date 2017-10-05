#!/usr/bin/env python
# coding=utf-8

# 实现arr.index(),对于已排序的list,二分查询.

arr = [1,4,5,8,10,12,14,33,36,44]
arr = range(10000)
res = 2334

start = 0
end = len(arr) - 1

count = 0
while True:
    count += 1
    mid = (end + start) / 2
    if arr[mid] > res:
        end = mid
    elif arr[mid] < res:
        start = mid
    else:
        print mid
        break
print count

print arr.index(222)