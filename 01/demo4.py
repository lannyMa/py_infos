#!/usr/bin/env python
# coding=utf-8

arr = [1, 2, 3, 2, 4]


def items__sec_index(op):
    if arr.count(op) >= 1:
        arr[arr.index(op)] = "%sop" % op
        index = arr.index(op)
        arr[arr.index(op)] = op
    return index


print items__sec_index(2)

arr = ['name','age']
print "".join(arr)