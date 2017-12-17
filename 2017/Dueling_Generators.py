class DuelingGenerator(object):
	def __init__(self, start_number, factor):
		self.number = start_number
		self.factor = factor
	
	def __call__(self):
		self.number = self.number * self.factor % 2147483647
		return self.number


if __name__ == "__main__":
	A = DuelingGenerator(516, 16807)
	B = DuelingGenerator(190, 48271)
	matches = 0
	for _ in range(40000000):
		if A() % 65536 == B() % 65536:
			matches += 1
	print(matches)
