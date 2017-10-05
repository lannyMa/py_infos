#!/usr/bin/env python
# coding=utf-8

f = open("user.txt",'w')

f.write("emy:1992\ncristin:1991\n")

f.writelines(["lanny:123\n","jack:1993\n","jobs:1888\n"])

f.close()