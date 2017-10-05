#!/usr/bin/env python
# coding=utf-8



def jiecheng(num):
    res = 1
    for i in range(num):
        res *= (i+1)
    return res

print jiecheng(4)