#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#


def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib <= c_road:
        return n*c_lib
    else:
        clusterId = 1
        clusters = {}
        knownCities = {}
        for [city1, city2] in cities:
            if city1 not in knownCities and city2 not in knownCities:
                knownCities[city1] = clusterId
                knownCities[city2] = clusterId
                clusters[clusterId] = [city1, city2]
                clusterId += 1
            elif city1 in knownCities and city2 not in knownCities:
                knownCities[city2] = knownCities[city1]
                clusters[knownCities[city1]].append(city2)
            elif city2 in knownCities and city1 not in knownCities:
                knownCities[city1] = knownCities[city2]
                clusters[knownCities[city2]].append(city1)
            elif city1 in knownCities and city2 in knownCities and knownCities[city1] != knownCities[city2]:
                # merge clusters
                cluster1 = knownCities[city1]
                cluster2 = knownCities[city2]
                for city in clusters[cluster2]:
                    knownCities[city] = cluster1
                clusters[cluster1].extend(clusters[cluster2])
                del clusters[cluster2]

        cost = sum((len(clusters[id]) - 1) * c_road for id in clusters)
        # create libraries for unreachable cities
        cost += c_lib * (len(clusters) + n - len(knownCities))

        return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(result)
        fptr.write(str(result) + '\n')

    fptr.close()
