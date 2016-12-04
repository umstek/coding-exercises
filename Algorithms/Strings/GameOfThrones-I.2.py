string = raw_input()
ltr = set(string)

found = sum([1 for l in ltr if (string.count(l) % 2 == 1)]) <= 1

if not found:
    print("NO")
else:
    print("YES")