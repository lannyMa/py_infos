#!/usr/bin/env python
# coding=utf-8

file_dict = {

}


# dict -> file
def write_file():
    tmp_list = []
    for user, pwd in file_dict.items():
        tmp_list.append("%s:%s\n" % (user, pwd))
    tmp_str = "".join(tmp_list)
    with open('user.txt', 'w') as f:
        f.write(tmp_str)


# file -> dict
def read_file():
    with open("user.txt") as f:
        for line in f:
            user, pwd = line.split(":")
            file_dict[user] = pwd.strip("\n")


