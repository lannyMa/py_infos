#!/usr/bin/env python
# coding=utf-8

file_dict={}

f=open("user.txt")
# 字符串
# print f.read()

# 读取一行,类型是字符串
print type(f.readline())

# 列表  每一行作为一项 添加到列表
print f.readlines()

