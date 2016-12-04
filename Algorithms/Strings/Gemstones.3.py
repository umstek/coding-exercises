import functools

compositions = [set(input().strip()) for i in range(int(input()))]
print(len(functools.reduce(lambda a, b: a & b, compositions)))
