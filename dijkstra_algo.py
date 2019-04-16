# 1 mark all nodes unvisited and then store them
# 2 set the distance to zero for our initial node and to infinity for other nodes
# 3 select unvisited node with smallest distance, it's the current node for now
# 4 find unvisited neighbours for current node and calculate their distances through the current node
# 	compare the newly calculated distance to the assigned and save the smaller one
# 5 mark the current node as visited and remove it from unvisited set
# 6 stop if the destination node has been visited or if the smallest distance among the unvisited nodes is infinity

from collections import deque, namedtuple

inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

def make_edge(start, end, cost=1):
	return Edge(start, end, cost)

class Graph:
	def __init__(self, edges):
		wrong_edges = [i for i in edges if len(i) not in [2,3]]
		if wrong_edges:
			raise ValueError('Wrong edges data: {}'.format(wrong_edges))

		self.edges = [make_edge(*edge) for edge in edges]

	@property
	def vertices(self):
		return set(
			sum(
				([edge.start, edge.end] for edge in self.edges), []				
			)
		)
		
	def get_node_pairs(self, n1, n2, both_ends=True):
		if both_ends:
			node_pairs = [[n1, n2], [n2, n1]]
		else:
			node_pairs = [[n1, n2]]
		return node_pairs

	def remove_edge(self, n1, n2, both_ends=True):
		node_pairs = self.get_node_pairs(n1, n2, both_ends)
		edges = self.edges[:]
		for edge in edges:
			if [edge.start, edge.end] in node_pairs:
				self.edges.remove(edge)

	def add_edge(self, n1, n2, cost=1, both_ends=True):
		node_pairs = self.get_node_pairs(n1, n2, both_ends)
		for edge in self.edges:
			if [edge.start, edge.end] in node_pairs:
				return ValueError('Edge {} {} already exists'.format(n1,n2))

		self.edges.append(Edge(start=n1, end=n2, cost=cost))
		if both_ends:
			self.edges.append(Edge(start=n2, end=n1, cost=cost))

	@property
	def neighbours(self):
		neighbours = {vertex: set() for vertex in self.vertices}
		for edge in self.edges:
			neighbours
		return neighbours

	def dijkstra(self, source, dest):
		assert source in self.vertices, 'Such source node doesn\'t exist'

		# 1 mark all nodes unvisited and store them
		# 2 set the distance to zero for our initial node
		# and to infinity for other nodes
		distances = {vertex: inf for vertex in self.vertices}
		previous_vertices = {
			vertex: None for vertex in self.vertices
		}
		distances[source] = 0
		vertices = self.vertices.copy()

		while vertices:
			# 3 select the unvisited node with the smallest distance,
			# it's current node now
			current_vertex = min(
				vertices, key=lambda vertex: distances[vertex])

			# 6 stop if the smallest distance among the node is infinity
			if distances[current_vertex] == inf:
				break

			# 4 find unvisited neighbours for the current node
			# and calculate their distances through the current node
			for neighbour, cost in self.neighbors[current_vertex]:
				alternative_route = distances[current_vertex] + cost

				# compare the newly calculated distance to the assigned and save the smaller one
				if alternative_route < distances[neighbour]:
					distances[neighbour] = alternative_route
					previous_vertices[neighbour] = current_vertex

			# 5 mark the current node as visited
			# and remove it from the unvisited set.
			vertices.remove(current_vertex)


		path, current_vertex = deque(), dest
		while previous_vertices[current_vertex] is not None:
			path.appendLeft(current_vertex)
			current_vertex = previous_vertices[current_vertex]
		if path:
			path.appendLeft(current_vertex)
		return path

def main():
	graph = Graph([
    ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
    ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
    ("e", "f", 9)])

	print(graph.dijkstra("a", "e"))
	deque(['a', 'c', 'd', 'e'])

main()