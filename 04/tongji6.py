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
    return sorted(res.items(), key=lambda x: x[1], reverse=True)


def get_html(arr):
    tmpl = "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"
    html_str = "<table border='1px'>"
    html_str += tmpl % ("No", "ip", "uri", "count")

    for index, r in enumerate(arr[:10]):
        html_str += tmpl % (index + 1, r[0][0], r[0][1], r[1])
        index += 1
    html_str += "</table>"
    return html_str


def start_operate():
    res = open_file()
    with open("access.html", 'w') as f:
        f.write(get_html(res))


start_operate()
