import math
import os
import random
import re
import sys

def pairs(k, arr):

    arr_set = set(arr)
    pair_set = set([x+k for x in arr])
    
    return len(arr_set.intersection(pair_set))
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

