# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/usr/bin/py
def height(n):
	if n == 0: return 1
	if n % 2 == 1: return 2*height(n-1)
	else: return height(n-1)+1

c = int(raw_input())
lst = [height(int(raw_input())) for i in range(c)]
for n in lst: print(n)