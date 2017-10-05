#!/usr/bin/env python
# coding=utf-8


## 让排序算法变得更加通用


def my_sort(arr, sort_fn):
    for j in range(11):
        for i in range(len(arr) - 1):
            if sort_fn(arr[i]) > sort_fn(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


############################################################
arr = [1, 2, 3, 4, 5, 1, 2, 3, 4, 6, 7, 22, 1212, 123, 2545]
def sort_fn1(data):
    return data

# 传进要排序的list + 传进去一个函数
print my_sort(arr, sort_fn1)

# sorted(arr,key=lambda x:x[1])
# print arr
############################################################
arr = [
    ("xiaohua", 100),
    ("xiaoming", 98),
    ("xiaohuang", 22),
    ("xiaoli", 22),
]

def sort_fn2(data):
    return arr[1]

print my_sort(arr,sort_fn2)