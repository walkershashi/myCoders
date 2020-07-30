#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the acmTeam function below.
def acmTeam(topic):
    
    comb = list(combinations([i for i in range(n)], 2))
    res = {}
    for i in comb:
        cnt = 0
        for bit in range(m):
            if topic[i[0]][bit] == '1' or topic[i[1]][bit]  == '1':
                cnt +=1
        if cnt not in res:
            res[cnt] = [i]
        else:
            res[cnt].append(i)
    mKey = max(res.keys())
    return([mKey, len(res[mKey])])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = sys.stdin.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
