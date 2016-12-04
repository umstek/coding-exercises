strings = [input().strip() for i in range(int(input()))]
for s in strings:
    if len(s) % 2 == 1:
        print(-1)
    else:
        s1 = s[:len(s) // 2]
        s2 = s[len(s) // 2:]
        dic = {}
        for c in s1:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for c in s2:
            if c in dic:
                dic[c] -= 1
            else:
                dic[c] = -1
        print(sum(abs(x) for x in dic.values()) // 2)