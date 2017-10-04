#!/usr/bin/env python
# coding=utf-8



# 1 * 2 * 3 * 4

def jiecheng(num):
    res = 1
    for i in range(num):
        res *= (i+1)
    return res

print jiecheng(0)