#!/usr/bin/env python
# coding=utf-8

# 读取文件,添加行号

num = 1
f = open("user.txt")
while True:
    line = f.readline()
    if line:
        line = line.rstrip("\n")
        name,pwd = line.split(":")
        print "%d -- %s %s"%(num,name,pwd)
        num += 1
    else:
        break