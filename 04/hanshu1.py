#!/usr/bin/env python
# coding=utf-8

# 函数内部找不到的变量会向外找
name = "maotai"

def hello():
    print "hello "+ name

hello()


def hello(name):
    print "hello "+ name

hello(" world")