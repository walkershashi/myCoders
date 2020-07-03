#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the pangrams function below.
def pangrams(s):
    s = s.lower()
    s = set(s)
    # There will be a space character in the set, So subtract one
    if len(s) - 1 == 26:
        return "pangram"

    else:
        return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

