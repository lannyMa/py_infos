#!/usr/bin/env python
# coding=utf-8

tmp = []
with open("access1.txt") as f:
    for line in f.readlines():
        tmp.append(line.split()[0])
print tmp



# list - dict : ip:count
d = {}
for ip in tmp:
    if ip in d.keys():
        d[ip] += 1
    else:
        d[ip] = 1

# dict   count:list[ip]
d2 = {}
for ip, count in d.items():
    d2.setdefault(count, [])
    d2[count].append(ip)

print d2.keys()

# 前10个ip html展示
# f = open('access.html','w')
# f.write("<html><table style='border:solid 1px'>")
# f.write("<th style='border:solid 1px'>访问次数</th><th style='border:solid 1px'>ip地址</th>")
#
# if len(d2.keys()) > 10:
#     for i in range(10):
#         key =  max(d2.keys())
#         for index in range(len(d2[key])):
#             f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key, d2[key][index]))
#         d2.pop(max(d2.keys()))
# else:
#     for i in range(len(d2.keys())):
#         key =  max(d2.keys())
#         for index in range(len(d2[key])):
#             f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key, d2[key][index]))
#         d2.pop(max(d2.keys()))

count = 0
f = open('access.html', 'w')
f.write("<html><head><meta charset='UTF-8'></head><table border='1px'>")

f.write("<th>访问次数</th><th>ip地址</th>")

while count < 10:
    key = max(d2.keys())
    for index in range(len(d2[key])):
        f.write('<tr><td>%s</td><td>%s</td></tr>' % (key, d2[key][index]))
    num = len(d2[key])
    d2.pop(key)
    count = count + num
f.write("</table></html>")
f.close()
