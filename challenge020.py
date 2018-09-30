from collections import namedtuple
struct = namedtuple

class Node:
	n_next = None
	val = None

	def __init__(self, val):
		self.val = val

class LinkedList:
	root = None
	last = None

	def add(self, val):
		if self.root == None:
			self.root = Node(val)
		elif self.last == None:
			n = Node(val)
			self.root.n_next = n
			self.last = n
		else:
			n = Node(val)
			self.last.n_next = n
			self.last = n

	def get(self, i):
		current_node = self.root
		for x in range(0, i):
			if(current_node.n_next == None):
				return None
			else:
				current_node = current_node.n_next
		return current_node

	def size(self):
		s = 1
		current_node = self.root
		while current_node.n_next != None:
				current_node = current_node.n_next
				s += 1
		return s


l_01 = LinkedList()
l_01.add(3);
l_01.add(7);
l_01.add(8);
l_01.add(10);

l_02 = LinkedList()
l_02.add(99);
l_02.add(1);
l_02.add(8);
l_02.add(10);

def get_result(l_01, l_02):
	hi_size = l_01.size()
	if(l_02.size() > hi_size):
		hi_size = l_02.size()
	for i in range(0, hi_size):
		if(l_01.get(i) == l_02.get(i)):
			return l_01.get(i)
	return None

print(get_result(l_01, l_02))