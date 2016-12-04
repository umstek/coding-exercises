trash = raw_input()
p = 0
n = 0
z = 0
for s in raw_input().split():
    i = int(s)
    if i > 0:
        p += 1
    elif i < 0:
        n += 1
    else:
        z += 1
        
total = p + n + z
print (p * 1.0 / total)
print (n * 1.0 / total)
print (z * 1.0 / total)