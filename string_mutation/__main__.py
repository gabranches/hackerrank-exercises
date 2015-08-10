# Enter your code here. Read input from STDIN. Print output to STDOUT
word = list(raw_input())
changes = raw_input().split()
word[int(changes[0])] = changes[1]

print "".join(word)