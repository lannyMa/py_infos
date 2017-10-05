#!/usr/bin/env python
# coding=utf-8

f = open("log.log")
ip_list = []
for line in f:
    ip_list.append(line.split()[0])

# list  -> dict
res = {}
for ip in ip_list:
    res[ip] = res.get(ip, 0) + 1

# sort

arr = res.items()
for j in range(11):
    for i in range(len(arr) - 1):
        if arr[i][1] > arr[i + 1][1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

html_str = "<table border='1px'><tr><th>No</th><th>ip</th><th>count</th></tr>"

count = 1
for ip in  arr[:-11:-1]:
    html_str+= "<tr><td>%s</td><td>%s</td><td>%s</td><tr>"%(count,ip[0],ip[1])
    # print "No%s, ip is %s, count is %s"%(count,ip[0],ip[1])
    count += 1
html_str+="</table>"

with open("access.html",'w') as f:
    f.write(html_str)
