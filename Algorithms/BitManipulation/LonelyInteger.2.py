#!/usr/bin/py
def lonelyinteger(a):
	s = set(a)
	b = a[:]
	for e in s: b.remove(e)
	for e in b: s.remove(e)
	return (list(s))[0]
if __name__ == '__main__':
	a = input()
	b = map(int, raw_input().strip().split(" "))
	print lonelyinteger(b)
