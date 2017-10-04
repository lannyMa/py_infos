#!/usr/bin/env python
# coding=utf-8

# 实现in
a = "i am maotai"

is_in = False

stra = "ma"
for s in a:
    if s == stra:
        is_in=True
        break
print is_in