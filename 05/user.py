#!/usr/bin/env python
# coding=utf-8

import fileutils

def zhuce():
    while True:
        name = raw_input("name: ").strip()
        fileutils.read_file()
        if len(name) == 0:
            print  "用户不能为空"
            continue
        if name in fileutils.file_dict:
            print "用户已存在"
            continue
        else:
            while True:
                pwd = raw_input("pwd: ").strip()
                if len(pwd) == 0:
                    print  "密码不能为空"
                else:
                    fileutils.file_dict[name]=pwd
                    fileutils.write_file()
                    break
            print "注册成功"
            break
# zhuce()

def denglu():
    name = raw_input("name: ")
    fileutils.read_file()
    if name not in fileutils.file_dict:
        print "用户名错误"
    else:
        pwd = raw_input("pwd: ")
        if fileutils.file_dict[name] == pwd:
            print "登录成功"
        else:
            print '密码错误'

denglu()