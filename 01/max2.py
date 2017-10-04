#!/usr/bin/env python
# coding=utf-8

# 找出列表中最大的2个

# 思路: 先遍历,找出第一个最大值,记录位置
# 再次遍历.找出次大的值,记录位置

arr = [1,65555,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45]

max_index = 0
for i in arr:
    if i > arr[max_index]:
        max_index = arr.index(i)
# print max_index
print max_index,arr[max_index]

max_index2=0
arr.pop(max_index)
for i in arr:
    if i > arr[max_index2]:
        max_index2 = arr.index(i)

print max_index2,arr[max_index2]