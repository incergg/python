import random

class RandomQueue:

	def __init__(self, size=10):
		self.n = size+1
		self.items = self.n * [None]
		self.head = -1

	def is_full(self):
		if self.n <= self.head+1:
			return True
		return False

	def is_empty(self):
		if self.head < 0:
			return True
		return False

	def insert(self, item):
		if self.is_full() == True:
			raise ValueError("Pelna kolejka!")
		self.items[self.head+1] = item
		self.head = self.head+1

	def remove(self):
		if self.is_empty():
			raise ValueError("Pusta kolejka!")
		if self.head == 0:
			temp = self.items[0]
			self.items[0] = None
			return temp
		else:
			temp2 = random.randint(0, self.head)
			temp = self.items[temp]
			self.items[temp] = self.items[self.head]
			self.items[self.head] = None
			self.head-=1
			return temp