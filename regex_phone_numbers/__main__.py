import re

n = int(raw_input())

nums = []

for _ in range(0, n):
	nums.append(raw_input())

for num in nums:
	p = re.compile(r'^[7-9][0-9]{9}$')
	m = p.match(num)
	if m:
		print 'YES'
	else:
		print 'NO'