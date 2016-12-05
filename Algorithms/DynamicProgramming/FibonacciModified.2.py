a, b, n = map(int, raw_input().strip().split())
def mfib(n):
	if n == 1: return a
	if n == 2: return b
	return mfib(n-1)**2 + mfib(n-2)
	
print(mfib(n))
