class Node:
    __slots__ = '_city', '_index', '_adjacentNodes'

    def __init__(self, index, city):
        self._city = city
        self._index = index
        self._adjacentNodes = {}             #  Create dictionary called adjacentNodes

    # Selector functions
    def getCity(self):
        return self._city

    def getIndex(self):
        return self._index

    def getAdjacentNodes(self):
        return self._adjacentNodes.keys()

    ############################               Fix later
    def addAdjacentNode(self, node, edgeIndex):
        self._adjacentNodes[node] = edgeIndex
    
    def firstAdjacentNode(self):
        return self._adjacentNodes[0].keys()
    ############################



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
        self.numNodes = 0
        self.nodeList = {}             #  Create dictionary of nodes called nodeList 

    def addNode(self, index, city):
        self.numNodes = self.numNodes + 1     # Increment number of nodes
        newNode = Node(index, city)           # Build instance of node class
        
#         Need to check if node exists already
        self.nodeList[index] = newNode
        return newNode
        
        
    def getNode(self, node):
        if node in self.nodeList:
            return self.nodeList[node]
        else:
            return None

    def addEdge(self, node1, node2, edgeCount):                        # node1 and node2 must already be created with addNode()
        self.nodeList[node1].addAdjacentNode(self.nodeList[node2], edgeCount)

    def getNodes(self):
        return self.nodeList.keys()

    def __iter__(self):
        return iter(self.nodeList.values())




if __name__ == '__main__':

#     Create instance of Graph class:
    g = Graph()
    
#     Begin indexing for edge and node
    edgeCount = 0
    nodeCount = 0

    # Open and read from file:
    file = open("graphSmall1.in")
    for i in file:
        i =i.strip('\n')
        i = i.split(" ")
        for line in i:
            nodeCount += 1
            edgeCount += 1
            line = line.split('-')
            node1 = g.addNode(nodeCount, line[0])
            node2 = g.addNode(nodeCount, line[1])
            node1Index = node1.getIndex()
            node2Index = node2.getIndex()
            g.addEdge(node1Index,node2Index,edgeCount)

#     print(g)
    for v in g:
        for w in v.getAdjacentNodes():
            print("( %s , %s )" % (v.getCity(), w.getCity()))







