#!/usr/bin/env python
# coding=utf-8


def open_file():
    f = open("log.log")
    ip_list = []
    for line in f:
        tmp = line.split()[0], line.split()[6]
        ip_list.append(tmp)
    res = {}
    for r in ip_list:
        res[r] = res.get(r, 0) + 1
    return res.items()

# list  -> dict

# sort
def bubble_sort():
    arr = open_file()
    for j in range(11):
        for i in range(len(arr) - 1):
            if arr[i][1] > arr[i + 1][1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
arr = bubble_sort()
# print arr[-1:-10:-1]


def write_html(arr):
    html_str = "<table border='1px'><tr><th>No</th><th>ip</th><th>uri</th><th>count</th></tr>"

    no = 1
    for r in arr[:-11:-1]:
        html_str += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><tr>" %(no, r[0][0], r[0][1], r[1])
        # print "No%s, ip is %s, uri is %s, count is %s"%(no, r[0][0], r[0][1], r[1])
        no += 1

    html_str += "</table>"

    with open("access.html", 'w') as f:
        f.write(html_str)
write_html(arr)

def start_operation():
    open_file()
    arr = bubble_sort()
    write_html(arr)

