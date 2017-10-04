#!/usr/bin/env python
# coding=utf-8

# bubble_sort
# 思路: 总共有n个数,冒泡n次, 从第一个数字开始冒泡

arr = [3,5,1,66,32,4]

for i in range(len(arr)):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

    print arr