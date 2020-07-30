#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    cnt = 0
    for i in s:
        if i == 'a':
            cnt += 1
    if n%len(s) == 0:
        return cnt * n//len(s)
    else:
        size = n//len(s)
        cnt *=size
        for i in range(n-size*len(s)):
            if s[i] == 'a':
                cnt +=1
        return cnt



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
