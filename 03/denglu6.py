#!/usr/bin/env python
# coding=utf-8

content = "who have touched their lives Love begins with a smile grows with a kiss and ends with a tear The brightest future will always be based on a forgotten past you can not go on well in life until you let go of your past failures and heartaches"

# str -> dict

d = {}

for word in content.split():
    if word in d.keys():
        d[word] += 1
    else:
        d[word] = 1
print d

d2 = {}                                                #将k,v互换，为num:list(word)格式
for word,count in d.items():
    d2.setdefault(count,[])
    d2[count].append(word)
print d2