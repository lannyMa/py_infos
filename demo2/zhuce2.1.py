#!/usr/bin/env python
# coding=utf-8

#----------------
# 注册模块
#----------------

while True:
    name = raw_input("name: ").strip()
    if len(name) == 0:
        print "用户名不能为null"
        continue

    pwd = raw_input("pwd: ").strip()
    pwd2 = raw_input("pwd: ").strip()
    if len(pwd) == 0 or pwd != pwd2:
        print "密码错误"
        continue
    else:
        with open("user.txt", "a+") as f:
            f.write("%s:%s\n" % (name, pwd))
        print "%s register sucessful" % name
        break

