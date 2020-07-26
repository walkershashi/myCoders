# Given a string and weights of all the alphabets find the 
#Special Point Average using the formula
#	SPA = (10 * E(C[ch] * W[ch]) ) / (TL * TW)
#	Where:
#	      C[ch]: Count of a character ch in S,
#             W[ch]: Weight of the character ch,
#             TL:   Total length of S and
#             TW:   Total Weight of unique characters of S


import collections

def SPA(arr, w):
    weights = {}
    for i in range(26):
        weights[chr(i + 97)] = w[i]

    counter = collections.Counter(arr)
    TL = len(arr)
    WL = 0
    for i in counter:
        WL += weights[i]
    sum_cnt_w = 0
    for i in counter:
        sum_cnt_w += counter[i] * weights[i]

    return '{:.2f}'.format((10 * sum_cnt_w) / (TL * WL)) 

t = int(input())
for _ in range(t):
    s = input()
    weights = list(map(int, input().split()))

    print(SPA(s, weights))
