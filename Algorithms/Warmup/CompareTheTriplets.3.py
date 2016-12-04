alice = list(map(int, input().strip().split()))
bob = list(map(int, input().strip().split()))
a = sum([1 for i in range(3) if alice[i] > bob[i]])
b = sum([1 for i in range(3) if alice[i] < bob[i]])

print(a, b)
