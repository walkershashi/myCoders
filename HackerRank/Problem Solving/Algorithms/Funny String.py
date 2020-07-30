#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    ascii_s = []
    ascii_rev_s = []
    for i in range(len(s)-1):
        ascii_s.append(abs(ord(s[i])-ord(s[i+1])))
        ascii_rev_s.append(abs(ord(s[::-1][i])-ord(s[::-1][i+1])))
    
    if ascii_s == ascii_rev_s:
        return "Funny"
    else:
        return "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()

