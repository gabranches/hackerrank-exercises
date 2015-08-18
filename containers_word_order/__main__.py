from collections import OrderedDict
n = int(raw_input())

word_list = OrderedDict([])
output = ''

for _ in xrange(0, n):
	word = raw_input()
	if word in word_list:
		word_list[word] += 1
	else:
		word_list.update({word:1})

print len(word_list)

for ans in word_list.values():
	output += str(ans) + ' '

print output.strip()