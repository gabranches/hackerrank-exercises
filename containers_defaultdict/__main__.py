from collections import defaultdict
n = raw_input().strip().split()

d = defaultdict(list)

for _ in xrange(0, int(n[0])):
	''' Build list A ''' 
	d['A'].append(raw_input())

for _ in xrange(0, int(n[1])):
	''' Build list B '''
	d['B'].append(raw_input())

for i in xrange(0, len(d['B'])):
	found_match = False
	matches = ''

	for k in xrange(0, len(d['A'])):
		if d['A'][k] == d['B'][i]:
			found_match = True
			matches += str(k + 1) + " "

	if found_match == False:
		print -1
	else:
		print matches.strip()
