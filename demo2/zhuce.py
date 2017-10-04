#!/usr/bin/env python
# coding=utf-8

#----------------
# 注册模块
#----------------

while True:
    name = raw_input("name: ").strip()
    pwd = raw_input("pwd: ").strip()
    pwd2 = raw_input("pwd: ").strip()
    if pwd != pwd2:
        print "密码不一致,re-enter"
        continue
    if name and pwd:
        with open("user.txt","a+") as f:
            f.write("%s:%s\n"%(name,pwd))
            print "%s register sucessful"%name
    else:
        print "user or pass emyty,reenter"