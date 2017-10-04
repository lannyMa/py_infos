#!/usr/bin/env python
# coding=utf-8


# 思路: 记录索引值
arr = [1, 65525, 2, 3, 2, 12, 3, 1, 3, 21, 2, 2, 3, 4111, 22, 3333, 444, 111, 4, 5, 777, 65555, 45, 33, 45]

max_num = 0
sec_num = 0
max_index = 0


i = 0
for num in arr:
    if num > max_num:
        max_num = num
        max_index = i
    i += 1


j = 0
for num in arr:
    if num > sec_num and j != max_index:
        sec_num = num
    j += 1
print max_num,sec_num
