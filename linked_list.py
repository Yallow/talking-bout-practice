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

	def size(self):
		node = self.head
		counter = 0
		while node != None:
			counter+=1
			node = node.get_next()
		return counter

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

	def sort_list(self, size):
		# use a bubble sort for this at the moment
		node = self.head
		l_length = size
		for _ in range(l_length):
			swapped = False
			node = self.head
			while node != None and node.get_next() != None:	
				if node.get_data() > node.get_next().get_data():
					# swap em
					holder = node.get_next().data
					node.get_next().data = node.data
					node.data = holder
					swapped = True
				node = node.get_next()
				
			if swapped == False:
				# we are done sorting
				return


		
new_l = LinkedList()
new_l.head = Node(22)
new_l.insert_end(11)
new_l.insert_front(44)
new_l.insert_end(200)
new_l.insert_end(2)
new_l.traverse()
new_l.sort_list(new_l.size())
new_l.traverse()
