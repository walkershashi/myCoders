#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    total_pages = 1
    page_questions = {}
    for i in range(1, len(arr)+1):
        ques_i = [j for j in range(1, arr[i-1] + 1)]
        cnt = 0
        if arr[i-1] % k == 0:
            for _ in range(arr[i-1] // k):
                page_questions[total_pages] = ques_i[cnt: k+cnt]
                cnt += k
                total_pages += 1
        else:
            for _ in range(arr[i-1] // k):
                page_questions[total_pages] = ques_i[cnt: k+cnt]
                cnt += k
                total_pages += 1
            page_questions[total_pages] = ques_i[cnt: k+cnt]
            total_pages += 1
    
    sp_questions = 0
    
    for page, ques in page_questions.items():
        if page in ques:
            sp_questions += 1
    
    return sp_questions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
