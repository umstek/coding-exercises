#!/bin/python3

import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)


def total(arr2d, x, y):
    return arr2d[x][y] + \
           arr2d[x - 1][y] + \
           arr2d[x - 1][y - 1] + \
           arr2d[x - 1][y + 1] + \
           arr2d[x + 1][y] + \
           arr2d[x + 1][y - 1] + \
           arr2d[x + 1][y + 1]


print(max([total(arr, x, y) for x in range(1, 5) for y in range(1, 5)]))
