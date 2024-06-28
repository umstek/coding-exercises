t = int(input().strip())


def solve_1():
    dev = {}
    ndev = [0]

    str_num = input().strip()
    num = int(str_num)

    for c in str_num:
        if c in dev:
            dev[c] += 1
        elif c in ndev:
            pass
        elif int(c) != 0 and (num % int(c) == 0):
            dev[c] = 1
        else:
            ndev += [c]
    print(sum(dev.values()))


for i in range(t):
    solve_1()