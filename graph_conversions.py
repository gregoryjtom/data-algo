#graph_conversions.py
"""
OUTLINE FOR CODE:
1) GRAPH DATA STRUCTURE DEFINITIONS - in graph_structures.py
2) CONVERTING FUNCTIONS - this file
	-> note: above every function is a complexity analysis
3) TESTS FOR FUNCTIONALITY - this file
note: used inspiration from textbook data structures
"""

#import objects from graph_structures.py
from graph_structures import adjacencyList, adjacencyMatrix, incidenceMatrix

"""
CONVERTING FUNCTIONS
"""

"""
a. Convert from an adjacency matrix to adjacency lists.
Complexity: O(n^2) since the algo must run insertEdge on the upper triangle of the nxn matrix.
This is without the checking if the edge has already been inserted. With checking insertion, 
the conversion could be O(n^2*m) due to O(m) worst case on checking if inserted already.
"""
def convertAdjMatrixToList(adjMatrix):
	n = adjMatrix.nvertices
	newList = adjacencyList(n)
	for i in range(n):
		for j in range(i,n):
			if adjMatrix.matrix[i][j]:
				newList.insertEdge(i,j,True)
	return newList

"""
b. Convert from an adjacency list to an incidence matrix.
Complexity: O(n+m) due to breadth first search meeting every vertex and edge in the graph once.
"""
def convertListToIncMatrix(adjList):
	nvertices = adjList.nvertices
	nedges = adjList.nedges
	newMatrix = incidenceMatrix(nvertices,nedges)
	#breadth first search, adding an edge every time a new edge is found
	bfsAndInsert(adjList,newMatrix)
	return newMatrix

def bfsAndInsert(adjList,incMatrix):
	n = adjList.nvertices
	discovered = [0] * n
	processed = [0] * n
	queue = []

	#loop through all vertices in case there are vertices not connected to the first
	for i in range(n):
		if not discovered[i]:
			queue.append(i)
			discovered[i] = 1
		#process each vertex one by one, breadth first search style by popping off queue
		while len(queue) > 0:
			v = queue.pop(0)
			curr = adjList.edges[v]
			#loop through all the adjacencies in the vertex
			while curr is not None:
				p = curr.vertex
				#if not processed, add edge to the matrix
				if not processed[p]:
					incMatrix.insertEdge(v,p)
				if not discovered[p]:
					queue.append(p)
					discovered[p] = 1
				curr = curr.next
			processed[v] = 1


"""
c. Convert from an incidence matrix to adjacency lists.
Complexity: O(n*m) due to worst case examining the entire array. 
If taking into account checking if edge has been inserted already, O(n*m^2) since
O(m) worst case on checking.
"""
def convertIncMatrixToList(incMatrix):
	nvertices = incMatrix.nvertices
	nedges = incMatrix.nedges
	newList = adjacencyList(nvertices)

	#go through all the edges and look for the vertices indicated as being part of the edge
	for i in range(nedges):
		x = -1
		y = -1
		for j in range(nvertices):
			if incMatrix.matrix[j][i]:
				if x != -1:
					y = j
					break
				else:
					x = j
		if x == -1 or y == -1:
			print("edge not detected")
		else:
			newList.insertEdge(x,y,True)
	return newList

"""
TESTS FOR FUNCTIONALITY (test letter corresponds to the function being tested)
"""

def testA():
	n = 20
	matrix = adjacencyMatrix(n)
	for i in range(n):
		for j in range(n):
			#random insertion of edges
			if (i+j) % 3 == 1:
				if i != j:
					matrix.insertEdge(i,j)
	print(matrix.matrix)
	li = convertAdjMatrixToList(matrix)
	for i in range(n):
		if li.edges[i] is not None:
			print(li.edges[i].vertex)

def testB():
	n = 20
	adjMatrix = adjacencyMatrix(n)
	for i in range(n):
		for j in range(n):
			#random insertion of edges
			if (i+j) % 3 == 1:
				if i != j:
					adjMatrix.insertEdge(i,j)
	li = convertAdjMatrixToList(adjMatrix)
	incMatrix = convertListToIncMatrix(li)
	print(incMatrix.matrix)

def testC():
	n = 20
	adjMatrix = adjacencyMatrix(n)
	for i in range(n):
		for j in range(n):
			#random insertion of edges
			if (i+j) % 3 == 1:
				if i != j:
					adjMatrix.insertEdge(i,j)
	li = convertAdjMatrixToList(adjMatrix)
	incMatrix = convertListToIncMatrix(li)
	converted_li = convertIncMatrixToList(incMatrix)
	if not converted_li.nedges == li.nedges:
		print("Number of edges has changed.")
	for i in range(n):
		if converted_li.edges[i] is not None:
			print(converted_li.edges[i].vertex)

if __name__ == "__main__":
	testA()
	testB()
	testC()


