#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    seqList = {}
    lastAnswer = 0
    res = []
    for query in queries:
        if query[0] == 1:
            index = (query[1] ^ lastAnswer) % n
            
            try:
                seqList[index].append(query[2])
            except:
                seqList[index] = [query[2]]
        
        else:
            index = (query[1] ^ lastAnswer) % n
            ele = query[2] % len(seqList[index])
            lastAnswer = seqList[index][ele]
            res.append(lastAnswer)
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

