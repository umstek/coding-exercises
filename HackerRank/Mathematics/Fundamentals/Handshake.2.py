c = input()
def nc2(n):
	if n <= 1: return 0
	return int((n / 2.0)*(n - 1))
	
lst = [nc2(input()) for _ in range(c)]
for i in lst: print(i)