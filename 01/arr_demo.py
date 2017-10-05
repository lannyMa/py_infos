#!/usr/bin/env python
# coding=utf-8

# 需求:
#   如果输入add,则需要用户输入add什么
#   如果输入do,干活,todo_list
#   如果什么都不输入,break

todo_list = []
while True:
    action = raw_input("add|do > ")
    if action == 'add':
        oper = raw_input("oper > ")
        todo_list.append(oper)
    elif action == "do":
        if len(todo_list):
            print todo_list.pop(0)
        else:
            print "nothing"
    else:
        break
