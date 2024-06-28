n, k = list(map(int, input().strip().split()))
num = sorted(list(map(int, input().strip().split())))

count = 0
for i in range(n - 1):
    rem_exp = (k - num[i] % k) % k
    count += len(list(filter(lambda x: x % k == rem_exp, num[i + 1:n])))

print(count)