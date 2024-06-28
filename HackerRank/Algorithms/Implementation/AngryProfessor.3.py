test_count = int(input())
for i in range(test_count):
    n, k = map(int, input().strip().split())
    arrivals = map(int, input().strip().split())
    print("NO" if len(list(filter(lambda a: a <= 0, arrivals))) >= k else "YES")