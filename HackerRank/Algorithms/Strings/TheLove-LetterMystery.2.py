#!/usr/bin/py
def changes(s):
	d = 0
	for i in range(len(s) // 2):
		d += abs(ord(s[i]) - ord(s[-i-1]))
	return d

c = int(raw_input())
lst = []
for i in range(c): lst.append(changes(raw_input()))

for i in lst: print(i)