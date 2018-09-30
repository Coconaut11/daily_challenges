class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(node):
	result = node.val

#	if node.left != None and node.right != None:
	if node.left != None:
		result = result + "," + serialize(node.left)
	else:
		result = result + ",None"
	if node.right != None:
		result = result + "," + serialize(node.right)
	else:
		result = result + ",None"
	return result

def deserialize(s):
	s = s.split(",")
	print(s)

print(serialize(node))
deserialize(serialize(node))