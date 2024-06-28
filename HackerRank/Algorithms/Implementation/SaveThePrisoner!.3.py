num_tests = int(input())
for i in range(num_tests):
    n, m, s = list(map(int, input().strip().split()))
    print(((m + s - 1 + n) % n + n - 1) % n + 1)
