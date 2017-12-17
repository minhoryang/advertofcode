class SpinLock(object):
	def __init__(self):
		self._data = [0]
		self.len = 1
		self.idx = 0

	def spin(self, next=3):
		for _ in range(next):
			self.idx += 1
			if self.idx == self.len:
				self.idx = 0
		return self._data[self.idx]

	def insert(self, data):
		self.len += 1
		self.idx += 1
		self._data.insert(self.idx, data)


if __name__ == "__main__":
	cl = SpinLock()
	hop = int(input())
	for i in range(2017):
		cl.spin(hop)
		cl.insert(i + 1)
	print(cl.spin(1))
