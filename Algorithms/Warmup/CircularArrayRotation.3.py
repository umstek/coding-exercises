n, k, q = list(map(int, input().strip().split()))
arr_n = list(map(int, input().strip().split()))

arr_r = arr_n[n - k % n:] + arr_n[:n - k % n]

for i in range(q):
    print(arr_r[int(input())])