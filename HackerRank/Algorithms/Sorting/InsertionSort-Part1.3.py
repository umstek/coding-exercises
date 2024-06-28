n = int(input())
arr = list(map(int, input().strip().split()))

stray = arr[n - 1]
index = n - 1
while index > 0 and arr[index - 1] > stray:
    arr[index] = arr[index - 1]
    print(" ".join(map(str, arr)))
    index -= 1

arr[index] = stray
print(" ".join(map(str, arr)))
