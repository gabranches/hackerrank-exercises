#!/bin/python3

import sys

n = int(input().strip())
c = sorted([int(c_temp) for c_temp in input().strip().split(' ')])

def countPairs(arr):
    if len(arr) < 2:
        return 0
    
    x1, x2, xs = arr[0], arr[1], arr[2:]
    
    if x1 == x2:
        return 1 + countPairs(xs)
    else:
        return countPairs([x2] + xs)
    
print(countPairs(c))  