import itertools as it
import operator as op

t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    arrcl = list(it.accumulate(arr, op.add))
    arrcr = list(reversed(list(it.accumulate(reversed(arr), op.add))))
    print("YES" if any([arrcl[r] == arrcr[r] for r in range(n)]) else "NO")
