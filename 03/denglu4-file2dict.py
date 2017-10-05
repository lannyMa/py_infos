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

while True:
    name = raw_input("name: ").strip()
    if not info.has_key(name):
        print "用户名不存在,请重新输入"
        continue

    flag = False
    for i in range(3):
        pwd = raw_input("pwd: ").strip()
        if info.get(name) == pwd:
            print "登录成功"
            flag = True
            break
        else:
            print "密码错误"
    else:
        break
    if flag:
        break