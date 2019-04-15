class Quick_Union:
	def __init__(self,n):
		self.id = list()
		self.sz = list()
		# set id of each object to itself
		for i in range(n):
			self.id.append(i)
			# initiate the size of all nodes
			self.sz.append(1)

	def root(self,i):
		# walk back to the root of i
		while i != self.id[i]:
			i = self.id[i]
		return i

	def connected(self,p,q):
		# this operation will get way to expensive right now
		# check if the root of two items are connected
		return self.root(p) == self.root(q)

	def union(self,p,q):
		# change root of p to point to root of q
		i = self.root(p)
		j = self.root(q)
		if i == j:
			return
		if self.sz[i] < sz[j]:
			self.id[i] = j
			self.sz[j] += self.sz[i]
		else:
			self.id[j] = i
			self.sz[i] += self.sz[j]
		self.id[i] = j

def main():
	boom = Quick_Union(10)
	print(boom.connected(6,9))
	boom.union(6,9)
	print(boom.connected(6,9))


main()