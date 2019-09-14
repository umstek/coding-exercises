#!/bin/python3

import math
import os
import random
import re
import sys


def birthdayCakeCandles(ar):
    freq = {}
    maxc = 0
    for a in ar:
        if maxc <= a:
            maxc = a
            if a in freq:
                freq[a] += 1
            else:
                freq[a] = 1
    return freq[maxc]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
