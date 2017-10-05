#!/usr/bin/env python
# coding=utf-8


info = {
    'name':'maxiaolang',
    'age':22
}

l = "test"
for line in dir(l):
    if line[:1] != "_":
        print line