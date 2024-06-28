n = int(raw_input())
matrix = [map(int, raw_input().split()) for i in range(n)]
major = sum([matrix[i][i] for i in range(n)])
anti = sum([matrix[i][-i-1] for i in range(n)])
print abs(major - anti)