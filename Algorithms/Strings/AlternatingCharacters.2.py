#!/usr/bin/py
def deletions(s):
	d = 0
	v = s[0]
	for i in range(1, len(s)):
		if s[i] == v: d+=1
		else: v = s[i]
	return d

c = int(raw_input())
lst = []
for i in range(c): lst.append(deletions(raw_input()))

for i in lst: print(i)