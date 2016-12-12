import re

text = raw_input()

ones        = "(IX|VI{,3}|IV|I{,3})"
tens        = "(XC|LX{,3}|XL|X{,3})"
hundreds    = "(CM|DC{,3}|CD|C{,3})"
thousands   = "(M{,3})"

p = re.compile(r'^' + thousands + hundreds + tens + ones + '$')

if p.match(text):
	print 'True'
else:
	print 'False'