t = input()

def product(l):
	p = 1
	for i in l: p *= i
	return p

lt = []
for i in range(t):
	n = input()
	ln = map(int, raw_input().strip().split())
	lt.append(product(ln) % 1234567)
	
for i in lt: print(i)