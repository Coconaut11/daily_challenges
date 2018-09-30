#NOT COMPLETED BUT IDGAF

class LinkedList:
    last = None
    root = None

    def add(self, val):
        node = Node(val)
        if self.root == None:
            self.root = node
            self.last = self.root
        else:
            self.last.n_next = node
            node.n_prev = self.last
            self.last = node

    def get(self, i):
        cnt = 0
        n_current = self.root
        while cnt < i:
            cnt = cnt + 1
            n_current = n_current.n_next
        return n_current.val
            

class Node:
    val = None
    n_next = None
    n_prev = None

    def __init__(self, val):
        self.val = val

list = LinkedList()
list.add(10)
list.add(20)
list.add(30)
list.add(40)
list.add(50)
print(list.get(0))
print(list.get(1))
print(list.get(2))
print(list.get(3))
print(list.get(4))
