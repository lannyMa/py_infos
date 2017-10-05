#!/usr/bin/env python
# coding=utf-8

# 读取文件,添加行号

# file -> dict

info = {}
with open("user.txt") as f:
    for line in f.readlines():
        name, pwd = line.split(":")
        info[name] = pwd.rstrip("\n")

print info

count=0
while True:
    count += 1
    if count > 3:
        print "错误超过3次"
        break
    name = raw_input("name: ").strip()
    if not info.has_key(name):
        print "用户不存在"
        continue

    pwd = raw_input("pwd: ").strip()
    if info.get(name) != pwd:
        print '密码错误'
        continue
    else:
        print "登录成功"
        break

