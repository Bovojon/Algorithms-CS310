class Node:
	__slots__ = '_city', '_index', '_adjacentNodes'

	def __init__(self, index, city):
		self._city = city
		self._index = index
		self._adjacentNodes = {}

	# Selector functions
	def getCity(self):
		return self._city

	def getIndex(self):
		return self._index

	def firstAdjacentNode(self):
		return self._adjacentNodes[0].keys()

	def getAdjacentNodes(self):
		return self._adjacentNodes.keys()

	def addNode(self, node, edgeIndex):
		self._adjacentNodes[node] = edgeIndex



class Edge:
	__slots__ = '_origin', '_destination', '_index'

	
	def __init__(self, u, v, index):
		self._origin = u
		self._destination = v
		self._index = index

	def getEndpoints(self):
		return (self._origin, self._destination)

	def getIndex(self):
		return self._index

	# Selector function
	def getOppositeNode(self, v):
		oppositeNode = self._destination
		return oppositeNode._index if v is self._origin else self._origin._index



class Graph:
	
	def __init__(self):
		self.nodeList = {}
		self.numNodes = 0

	def addNode(self, index, city):
		self.numNodes = self.numNodes + 1
		newNode = Node(index, city)
		self.nodeList[index] = newNode
		return newNode

	def getNode(self, node):
		if node in self.nodeList:
			return self.nodeList[node]
		else:
			return None

	def addEdge(self, u, v, edgeCount):
		edgeCount = edgeCount + 1
		if u not in self.nodeList:
			newNode = self.addNode[u]
		if v not in self.nodeList:
			newNode = self.addNode[v]
		self.nodeList[u].addNode(edgeCount, self.nodeList[v])


	def getNodes(self):
		return self.nodeList.keys()

	def __iter__(self):
		return iter(self.nodeList.values())




if __name__ == '__main__':
	g = Graph()
	cities = ['J', 'K', 'L', 'O']
	for i in range(6):
		for city in cities:
			g.addNode(i, city)

	print(g.nodeList)

	print("----------------------------------")

	edgeCount = 0
	g.addEdge(0,1, edgeCount)
	g.addEdge(0,5, edgeCount)
	g.addEdge(1,2, edgeCount)
	g.addEdge(2,3, edgeCount)
	g.addEdge(3,4, edgeCount)
	g.addEdge(3,5, edgeCount)
	g.addEdge(4,0, edgeCount)
	g.addEdge(5,4, edgeCount)
	g.addEdge(5,2, edgeCount)

	for v in g:
		for c in v.getAdjacentNodes():
			print("( %s , %s )" % (v.getIndex(), c.getIndex()))










