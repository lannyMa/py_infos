#!/usr/bin/env python
# coding=utf-8

arr1 = [1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
arr2 = [2,1,3,2,43,234,454,452,234,14,21,14]

new_arr = []

for i in arr2:
    if i in arr1 and i not in new_arr:
        new_arr.append(i)

print new_arr