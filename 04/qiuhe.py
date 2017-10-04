#!/usr/bin/env python
# coding=utf-8

def sum2(*num):
    res = 0
    for i in num:
        res += i
    return res

print sum2(1,2,3,4)