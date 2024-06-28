k = int(input())
arr = list(map(int, input().strip().split()))

shifts = 0
for n in range(1, k):
    stray = arr[n]
    index = n
    while index > 0 and arr[index - 1] > stray:
        arr[index] = arr[index - 1]
        shifts += 1
        # print(" ".join(map(str, arr)))
        index -= 1

    arr[index] = stray
    # print(" ".join(map(str, arr)))
print(shifts)
