from functools import reduce

grades = []
c, r = input().split(' ')

for i in range(0, int(r)):
    grades.append([float(x) for x in input().split()])
    
for grades in list(zip(*grades)):
    print(reduce(lambda x,y: x + y, grades)/int(r))