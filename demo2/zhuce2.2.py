#!/usr/bin/env python
# coding=utf-8

#----------------
# 注册模块
#----------------

## 实现连续输入3次密码错误后不允许注册---放在登录模块实现

while True:
    name = raw_input("name: ").strip()
    if len(name) == 0:
        print "用户名不能为null"
        continue

    # 实现3次密码输错,退出
    count = 0
    for i in range(3):
        count = i+1
        pwd = raw_input("pwd: ").strip()
        pwd2 = raw_input("pwd: ").strip()
        if len(pwd) == 0 or pwd != pwd2:
            print "密码错误"
        else:
            break
    if count == 3:
        print "gou l, fuck!!"
        break

    # 如果以上信息判断没问题,则写入
    with open("user.txt", "a+") as f:
        f.write("%s:%s\n" % (name, pwd))
    print "%s register sucessful" % name
    break
