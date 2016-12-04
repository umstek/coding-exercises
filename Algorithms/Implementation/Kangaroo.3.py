#!/bin/python3

x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if v1 == v2:
    print("YES" if x1 == x2 else "NO")
else:
    n = (x1 - x2)//(v2 - v1)
    nf = (x1 - x2)/(v2 - v1)
    print("YES" if n > 0 and n == nf else "NO")