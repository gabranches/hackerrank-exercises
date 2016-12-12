n_m = raw_input().strip().split()

int_list = raw_input().strip().split()

set_a = set(raw_input().strip().split())
set_b = set(raw_input().strip().split())

happiness = 0

for i in int_list:
	if i in set_a:
		happiness += 1
	if i in set_b:
		happiness -= 1

print happiness