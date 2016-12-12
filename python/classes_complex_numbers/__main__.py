class Complex(object):

	def __init__(self, real, complex):
		self.real = float(real)
		self.complex = float(complex)

	def __add__(n1, n2):
		'''Adds two complex numbers'''
		return Complex(n1.real + n2.real, n1.complex + n2.complex)

	def __sub__(n1, n2):
		'''Subtracts two complex numbers'''
		return Complex(n1.real - n2.real, n1.complex - n2.complex)

	def __mul__(n1, n2):
		'''Multiplies two complex numbers'''
		return Complex(n1.real * n2.real - n1.complex * n2.complex, 
				n1.real * n2.complex + n2.real * n1.complex)

	def __div__(n1, n2):
		'''Divides two complex numbers'''
		conj = n2.conjugate()
		numerator = n1 * conj
		denominator = float((n2 * conj).real)
		return Complex(numerator.real / denominator, numerator.complex / denominator)

	def fmt(self, n):
		'''Format complex number output'''
		return "{0:.2f}".format(round(n, 2))	

	def __str__(self):
		if self.complex == float(0):
			return self.fmt(self.real)
		elif self.real == float(0):
			return self.fmt(self.complex) + 'i'
		elif self.complex > 0:
			return self.fmt(self.real) + " + " + self.fmt(self.complex) + 'i'
		else:
			return self.fmt(self.real) + " - " + "{0:.2f}".format(round(abs(self.complex), 2)) + 'i'
	
	def conjugate(self):
		'''Conjugates a complex number'''
		return Complex(self.real, -self.complex)

	def mod(self):
		'''Returns the modulus of a complex number'''
		return Complex(((self.real ** 2 + self.complex ** 2) ** 0.5), 0)

n1 = raw_input().strip().split()
n2 = raw_input().strip().split()

n1 = Complex(n1[0], n1[1])
n2 = Complex(n2[0], n2[1])

print n1 + n2
print n1 - n2
print n1 * n2
print n1 / n2
print n1.mod()
print n2.mod()