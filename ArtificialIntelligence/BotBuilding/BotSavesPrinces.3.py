#!/usr/bin/python
def display_path_to_princess(n, grid):
    p, m = None, None
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                p = (i, j)
                if p is not None and m is not None:
                    break
            if grid[i][j] == 'm':
                m = (i, j)
                if p is not None and m is not None:
                    break

    a, b = m[0] - p[0], m[1] - p[1]
    if a < 0:
        for aa in range(abs(a)):
            print("DOWN")
    else:
        for aa in range(a):
            print("UP")

    if b < 0:
        for aa in range(abs(b)):
            print("RIGHT")
    else:
        for aa in range(b):
            print("LEFT")


g = int(input())
grid = []
for k in range(0, g):
    grid.append(input().strip())

display_path_to_princess(g, grid)
