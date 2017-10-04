#!/usr/bin/env python
# coding=utf-8

content = "who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on a forgotten past you can not go on well in life until you let go of your past failures and heartaches"

# str - list - dict
d = {}
for word in content.split():
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1

# dict:  v:list[k]
d2 = {}
for word,count in d.items():
    d2.setdefault(count,[])
    d2[count].append(word)
print d2


