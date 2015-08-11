n = int(raw_input())

fib_list = []

for i in range(0, n):
	if i == 0:
		fib_list.append(i)
	elif i == 1:
		fib_list.append(i)
	else:
		fib_list.append(fib_list[i-1] + fib_list[i-2])

cube = lambda x: x ** 3

print map(cube, fib_list)