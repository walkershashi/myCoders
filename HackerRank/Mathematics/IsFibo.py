#!/usr/bin/env python3

import os
import sys

# Complete the solve function below.
def solve(n):
    a = 0
    b = 1
    while a < n:
        a, b = b, a+b
        if n == a or n == b:
            return "IsFibo"
    
    return "IsNotFibo"

if __name__ == '__main__':
    
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        print(result)
