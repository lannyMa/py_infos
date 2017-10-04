#!/usr/bin/env python
# coding=utf-8

# 读取文件,添加行号

with open("user.txt") as f:
    count = 0
    for line in f.readlines():
        count += 1
        name,pwd = line.split(":")
        print "%d---> %s  %s"%(count,name,pwd.strip("\n"))