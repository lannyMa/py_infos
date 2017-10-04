#!/usr/bin/env python
# coding=utf-8

arr = [3, 5, 1, 66, 32, 4]

for i in range(len(arr) - 1):

    print "*"*30
    print i
    print "*"*30

    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            print "%s > %s " % (arr[i], arr[i + 1])
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print arr
        else:
            print "%s < %s" % (arr[i], arr[i + 1])
            print arr
print arr


# ******************************
# 0
# ******************************
# 3 < 5
# [3, 5, 1, 66, 32, 4]
# 5 > 1
# [3, 1, 5, 66, 32, 4]
# 5 < 66
# [3, 1, 5, 66, 32, 4]
# 66 > 32
# [3, 1, 5, 32, 66, 4]
# 66 > 4
# [3, 1, 5, 32, 4, 66]