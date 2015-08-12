'''
Note: I did not use the itemgetter library. 
Instead, I use the sort_directory function below to sort the directory.
'''

import re

people = []
n = int(raw_input())

for _ in range(0, n):
	person = raw_input().strip()
	p = re.compile(r'([a-z ]+)\s(\d+)\s(\w)', re.I)
	m = p.match(person)
	if m:
		people.append([m.group(1), m.group(2), m.group(3)])

def formalize(func):
	def add_prefix(*args, **kwargs):
		people = func(*args, **kwargs)
		new_people = []
		for person in people:
			if person[2] == 'M':
				new_people.append("Mr. " + person[0])
			else:
				new_people.append("Ms. " + person[0])	
		return new_people			
	return add_prefix

@formalize
def sort_directory(directory):
	'''Sorts the directory by age'''
	new_directory = []
	if len(directory) == 1:
		return directory
	for person in directory:
		if len(new_directory) == 0:
				new_directory.append(person)
		else:
			for k in range(0, len(new_directory)):
				if new_directory[k][1] > person[1]:
					new_directory.insert(k, person)
					break
				elif k == len(new_directory)-1:
					new_directory.append(person)
					break
	return new_directory

for person in sort_directory(people):
	print person
