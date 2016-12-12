#!/bin/python3

import sys

S = input().strip()

def count_diffs(sos):
    diffs = 0
    if sos[0] != 'S':
        diffs += 1
    if sos[1] != 'O':
        diffs += 1
    if sos[2] != 'S':
        diffs += 1
    return diffs
    
def analyze_sos(s):
    if len(s) == 3:
        return count_diffs(s)
   
    x, xs = s[:3], s[3:]
    
    return count_diffs(x) + analyze_sos(xs)
    
print(analyze_sos(S))