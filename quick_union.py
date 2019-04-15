class Quick_Union:
	def __init__(self,n):
		self.id = list()
		# set id of each object to itself
		for i in range(n):
			self.id.append(i)

	def root(self,i):
		# walk back to the root of i
		while i != self.id[i]:
			i = self.id[i]
		return i

	def connected(self,p,q):
		# check if the root of two items are connected
		return self.root(p) == self.root(q)

	def union(self,p,q):
		# change root of p to point to root of q
		i = self.root(p)
		j = self.root(q)
		self.id[i] = j

def main():
	boom = Quick_Union(10)
	print(boom.connected(6,9))
	boom.union(6,9)
	print(boom.connected(6,9))


main()