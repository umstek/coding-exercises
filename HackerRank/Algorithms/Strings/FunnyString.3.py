import functools

strings = [input().strip() for i in range(int(input()))]
for s in strings:
    funf = [abs(ord(s[i]) - ord(s[i - 1])) == abs(ord(s[len(s) - i]) - ord(s[len(s) - i - 1])) for i in
            range(1, len(s))]
    print("Funny" if functools.reduce(lambda a, b: a and b, funf) else "Not Funny")
