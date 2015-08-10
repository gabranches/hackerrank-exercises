# Enter your code here. Read input from STDIN. Print output to STDOUT

class Complex(object):

	def __init__(self, real, complex):
		self.real = real
		self.complex = complex

	def __add__(n1, n2):
		return Complex(n1.real + n2.real, n1.complex + n2.complex)

	def __sub__(n1, n2):
		return Complex(n1.real - n2.real, n1.complex - n2.complex)

	def __mul__(n1, n2):
		return Complex(n1.real * n2.real - n1.complex * n2.complex, 
				n1.real * n2.complex + n2.real * n1.complex)

	def __div__(n1, n2):
		conj = n2.conjugate()
		numerator = n1 * conj
		denominator = float((n2 * conj).real)
		return Complex(numerator.real / denominator, numerator.complex / denominator)

	def __str__(self):
		if self.complex == float(0):
			return format_imaginary(self.real)
		elif self.real == float(0):
			return format_imaginary(self.complex) + 'i'
		elif self.complex > 0:
			return  format_imaginary(self.real) + " + " + format_imaginary(self.complex) + 'i'
		else:
			return format_imaginary(self.real) + " - " + format_imaginary(abs(self.complex))+ 'i'

	def conjugate(self):
			return Complex(self.real, -self.complex)


def format_imaginary(s):
	return "{0:.2f}".format(round(float(s), 2))


def mod(n):
	return Complex(((n.real ** 2 + n.complex ** 2) ** 0.5), 0)


n1 = map(float, raw_input().split())
n2 = map(float, raw_input().split())

n1 = Complex(n1[0], n1[1])
n2 = Complex(n2[0], n2[1])

print n1 + n2
print n1 - n2
print n1 * n2
print n1 / n2
print mod(n1)
print mod(n2)