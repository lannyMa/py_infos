#!/usr/bin/env python
# coding=utf-8

file_dict = {}

# file => dict
def read_file():
    with open("user.txt") as f:
        for line in f.readlines():
            user,pwd = line.split()
            file_dict[user]=pwd
    return file_dict


# dict => file
def write_file():
    file_list=[]
    for user, pwd in file_dict.items():
        file_list.append("user pwd\n" % (user, pwd))

    with open("user.txt",w) as f:
        f.write("\n".join(file_list))
