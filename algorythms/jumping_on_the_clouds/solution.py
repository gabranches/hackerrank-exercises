#!/bin/python3

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

def jump(c):   
    
    if len(c) == 1:
        return 0
    if len(c) == 2 or len(c) == 3:
        return 1
    
    x1, x2, xs = c[1], c[2], c[3:]
    
    if x1 == 0 and x2 == 0 or x1 == 1:
        return 1 + jump([x2] + xs)
    
    if x1 == 0:
        return 1 + jump([x1] + [x2] + xs)
    
print(jump(c))