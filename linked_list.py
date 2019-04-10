class Node:
	def __init__(self, data=None, next_node=None):
		self.data = data
		self.next_node = next_node

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def traverse(self):
		node = self.head
		while node != None:
			print(node.get_data())
			node = node.get_next()

	def insert_front(self, data):
		new_node = Node(data)
		new_node.set_next(self.head)
		self.head = new_node

	def insert_end(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
			return
		c_node = self.head
		while c_node.get_next():
			c_node = c_node.get_next()
		c_node.set_next(new_node)
		
new_l = LinkedList()
new_l.head = Node(22)
new_l.insert_end(11)
new_l.insert_front(44)
new_l.traverse()
