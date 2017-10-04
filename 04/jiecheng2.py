#!/usr/bin/env python
# coding=utf-8


def jiecheng(num):
    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res


print jiecheng(4) + jiecheng(4)
