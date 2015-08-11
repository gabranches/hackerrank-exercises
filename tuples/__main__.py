a = int(raw_input())
b = raw_input()
b_list = b.split(' ')

print hash(tuple(map(int, b_list)))