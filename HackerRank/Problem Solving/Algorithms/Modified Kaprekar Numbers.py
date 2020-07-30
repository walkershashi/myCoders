#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    kaprekarNums = []
    for i in range(p, q+1):
        n = str(i*i)
        d = len(n)
        r_len = len(str(i))
        r = n[-r_len: ]
        l = n[: -r_len]
        if len(l) == 0:
            l = '0'
        if int(l) + int(r) == i:
            kaprekarNums.append(i)
    if len(kaprekarNums) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(map(str, kaprekarNums)))



if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)

