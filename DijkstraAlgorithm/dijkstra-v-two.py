# 1) Plot out the graph
# 2) Apply Dijkstra's Algorithm
# 3) Print routing table

import collections

# Build a Graph class:
class Graph:
	def __init__(self):
		self.nodes = set()
		self.edges = collections.defaultdict(list)
		self.distances = {}

	def add_node(self, value):
		self.nodes.add(value)

	def add_edge(self, from_node, to_node, distance):
		self.edges[from_node].append(to_node)
		self.edges[to_node].append(from_node)
		self.distances[(from_node, to_node)] = distance


# Build the graph from input file
def buildGraph():
	g = Graph()

	file = open("one.net", "r")
	for line in file.readlines():
		g.add_node(line[0])
		g.add_node(line[1])
		g.add_edge(line[0], line[1], line[2])

	file.close();

	return g


# Apply Dijkstra's algorithm
def dijkstra(graph, start):
	visited = {start: 0}
	path = {}

	unvisited = set(graph.nodes)

	while unvisited:
		min_node = None
		for node in unvisited:
			if node in visited:
				if min_node is None:
					min_node = node
				elif visited[node] < visited[min_node]:
					min_node = node
		if min_node is None:
			break

		node.remove(min_node)
		current_weight =visited[min_node]

		for edge in graph.edges[min_node]:
			weight = current_weight + graph.distances[(min_node, edge)]
			if edge not in visited or weight < visited[edge]:
				visited[edge] = weight
				path[edge] = min_node

	return visited, path


if __name__ == "__main__":
	try:

		graph = buildGraph()
		visited, path = dijkstra(graph, graph.nodes[0])
		print(visited)

	except TypeError as t:
		print(t)