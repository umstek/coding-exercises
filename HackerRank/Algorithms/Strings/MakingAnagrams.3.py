store = {}

for c in input():
    if c in store:
        store[c] += 1
    else:
        store[c] = 1

for c in input():
    if c in store:
        store[c] -= 1
    else:
        store[c] = -1

print(sum(map(abs, store.values())))