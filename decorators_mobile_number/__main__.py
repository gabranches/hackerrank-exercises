n = int(raw_input())
numbers = []

for _ in range(0, n):
	numbers.append(raw_input())

def number_standardizer(func):
	def add_prefix(*args, **kwargs):
		return [ "+91 " + x[:5] + ' ' + x[-5:] for x in func(*args, **kwargs) ]
	return add_prefix

@number_standardizer
def sort_numbers(numbers):
	return sorted([x[-10:] for x in numbers])

for num in sort_numbers(numbers):
	print num