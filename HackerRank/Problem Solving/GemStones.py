#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    set_ = set(arr[0])
    for i in range(len(arr)):
        set_.intersection_update(arr[i])
        
    return(len(set_))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

