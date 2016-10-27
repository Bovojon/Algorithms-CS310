import copy


class Edges:
	def __init__(self, nodeA, nodeB, cost):
		self.cost = cost
		self.nodeA = nodeA
		self.nodeB = nodeB

######################################################

def removeVisited(node, unvisited):
	k = 0
	for u in unvisited:
		if u == node:
			del unvisited[k]
			return
		k = k+1


######################################################

def checkIfNodeExits(node, verticesArray):
	for vertex in verticesArray:
		if vertex == node:
			return True
	return False

######################################################

def Dijkstra(edgesArray, verticesArray, start):
	# Create 3 empty sets and an empty array:
	previous= {}
	dist = {}
	route = {}
	unvisited = []

	for vertex in verticesArray:
		previous[vertex] = -1			# Previous node from source
		dist[vertex] = float('inf')			# Unknown distance from source to vertex - set to inifinity initially
		route[vertex] = [start]				# Add the source to the path			
		unvisited.append(vertex)			# Initially, all nodes are in the unvisited set

	dist[start] = 0
	route[start].append(-1)					# No route exists between the source and itself, so set route to -1
	while len(unvisited) != 0:
		x = None
		dist_x = float('inf')

		for u in unvisited:
			if dist[u] < dist_x:
				dist_x = dist[u]
				x = u
		removeVisited(x, unvisited)

		for edge in edgesArray:

			if x == edge.nodeA:
				new_dist = dist[x] + int(edge.cost)
				if new_dist < dist[edge.nodeB]:
					previous[edge.nodeB] = edge.nodeB
					dist[edge.nodeB] = new_dist
					if x!= start:
						route[edge.nodeB] = copy.deepcopy(route[x])
					route[edge.nodeB].append(edge.nodeB)

			elif x == edge.nodeB:
				new_dist = dist[x] + int(edge.cost)
				if new_dist < dist[edge.nodeA]:
					previous[edge.nodeA] = edge.nodeA
					dist[edge.nodeA] = new_dist
					if x != start:
						route[edge.nodeA] = copy.deepcopy(route[x])
					route[edge.nodeA].append(edge.nodeA)
	dist_sort = sorted(dist)
	for d in dist_sort:
		if route[d][1] == -1:
			print '  Source: ', start, '  Destination: ', d, '  Route: ', route[d][1], '  Cost: ', dist[d]
		else:
			print '  Source: ', start, '  Destination: ', d, '  Route: ', route[d][1], '   Cost: ', dist[d]

######################################################

def main():
	print("Jon")
	print("CS410 - Dijkstra's Algorithm")
	verticesArray = []
	edgesArray = []				# edgesArray is an array of instances of Edges class 

	# Open file
	file = open('/home/jon/Desktop/C/DijkstraAlgorithm/zero.net', 'r')
	link_count = 0

	# Read lines of file and add to edgesArray
	for line in file:
		index = line.split(' ')
		edgesArray.append(Edges(index[0], index[1],index[2]))
		link_count += 1
		print "Node A: ",index[0], " Node B: ", index[1], "Cost: ", int(index[2])
	
	# For each edge, add its nodes to the verticesArray
	for edge in edgesArray:
		if checkIfNodeExits(edge.nodeA, verticesArray) != True:
			verticesArray.append(edge.nodeA)
		if checkIfNodeExits(edge.nodeB, verticesArray) != True:
			verticesArray.append(edge.nodeB)

	verticesArray.sort()
	print "Link count: ", link_count, "Node Count: ", len(verticesArray)
	
	# Apply Dijkstra's Algorithm to each vertex in verticesArray
	for vertex in verticesArray:
		Dijkstra(edgesArray, verticesArray, vertex)



if __name__ == '__main__':
	main()



















