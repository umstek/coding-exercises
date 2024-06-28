#!/usr/bin/py
n = input()
k = input()
candies = [input() for _ in range(n)]
candies.sort()
min_diff = min([(candies[k+i-1] - candies[i]) for i in range(len(candies) - k+1)])

print min_diff
