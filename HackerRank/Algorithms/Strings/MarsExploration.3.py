s = input().strip()

print(sum([sum([s[i * 3] != 'S', s[i * 3 + 1] != 'O', s[i * 3 + 2] != 'S']) for i in range(len(s) // 3)]))
