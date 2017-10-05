#!/usr/bin/env python
# coding=utf-8

# 实现去重


arr = [1,2,2,2,2,2,2,2,2,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]

for i in range(len(arr)):
    for j in arr:
        if arr.count(j)>1:
            arr.pop(j)

print arr