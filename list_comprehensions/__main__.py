# Enter your code here. Read input from STDIN. Print output to STDOUT

input = []

for i in range(0,4):
    input.append(int(raw_input()))

L = [[x,y,z] for x in range(0,input[0]+1) for y in range(0,input[1]+1) for z in range(0,input[2]+1) if x + y + z <> input[3]]

print L