#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    len_ = len(s) // 3
    org_msg = 'SOS' * len_
    
    cnt = 0
    for org_i, s_i in zip(org_msg, s):
        if org_i != s_i :
            cnt += 1
    
    return cnt
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

