#!/usr/bin/env python
# coding=utf-8

file_dict = {}

f = open("user.txt")

# print f.read().split("\n")

for line in f.readlines():
    k,v = line.split()
    file_dict[k]=v

print file_dict