#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the equalizeArray function below.
def equalizeArray(arr):
    counter = collections.Counter(arr)
    maxes = counter.values()
    cnt = sum(maxes) - max(maxes)
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
