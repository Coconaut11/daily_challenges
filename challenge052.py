class Cache:

	def __init__(self, n):
		self.n = n
		self.container = {}
		self.uses = []

	def set(self, key, value):
		if len(self.container) >= self.n:
			del self.container[uses[0]]
			del self.uses[0]
		self.container[key] = value
		uses.append(key)
		shift(uses, -1)

	def get(self, key):
		it = self.container[key]
		if it != None:
			return it
			
		else
			return None

	def print_len(self):
		print(len(self.container))

cache = Cache(3)

cache.set("apples", 10)
cache.print_len()
cache.set("mand", 12)
cache.print_len()
cache.set("pears", 12)
cache.print_len()
cache.set("peacocks", 11)
cache.print_len()
