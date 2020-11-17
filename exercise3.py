"""
OUTLINE FOR CODE:
1) GRAPH DATA STRUCTURE DEFINITIONS
2) CONVERTING FUNCTIONS
	-> note: above every function is a complexity analysis
3) TESTS FOR FUNCTIONALITY

Adjacency Matrix: We can represent G using an n × n matrix M, where
element M[i, j] = 1 if (i, j) is an edge of G, and 0 if it isn’t.
"""

"""
GRAPH DATA STRUCTURE DEFINITIONS
"""

class adjacencyList:
	def __init__(self,nvertices):
		self.nvertices = nvertices
		#start with no edges, must insert using function below
		self.nedges = 0
		#assume vertices numbering starts at 0
		self.edges = [None]*nvertices

	def insertEdge(self,x,y,first):
		#create new node and set next to the existing list of nodes
		newEdge = edgeNode(y)
		newEdge.next = self.edges[x]
		self.edges[x] = newEdge
		#boolean first determines whether the second direction of the undirected edge needs to be added
		if first:
			self.insertEdge(y,x,False)
		else:
			self.nedges += 1

	class edgeNode:
		def __init__(self,vertex):
			self.vertex = vertex
			self.next = None

class adjacencyMatrix:
	def __init__(self,nvertices):
		#initialize 2d array of zeros
		self.matrix = [ [0] * nvertices for _ in range(nvertices)]
		self.nvertices = nvertices
		self.nedges = 0

	def insertEdge(self,x,y):
		#check if edge is already present (must use x-1 and y-1 since numbering starts at 0 for array)
		if not self.matrix[x][y]:
			self.matrix[x][y] = 1
			#since undirected, set y,x to 1 as well
			self.matrix[y][x] = 1
			self.nedges += 1

class incidenceMatrix:
	def __init__(self,nvertices,nedges):
		self.nvertices = nvertices
		self.nedges = nedges
		#member variable to keep track of which column to add next edge to:
		self.nextEdge = 0
		#initialize 2d array of zeros 
		self.matrix = [ [0] * nedges for _ in range(nvertices)]

	def insertEdge(self,x,y):
		#change the correct vertices to 1 to indicate an edge
		self.matrix[x][self.nextEdge] = 1
		self.matrix[y][self.nextEdge] = 1
		#increment the counter
		self.nextEdge += 1

"""
CONVERTING FUNCTIONS
"""
"""
a. Convert from an adjacency matrix to adjacency lists.
Complexity:
"""
def convertAdjMatrixToList(adjMatrix):
	n = adjMatrix.nvertices
	newList = adjacencyList(n)
	for i in range(n):
		for j in range(i,n):
			if adjMatrix.matrix[i,j]:
				newList.insertEdge(i,j,True)
	return newList

"""
b. Convert from an adjacency list to an incidence matrix.
Complexity:
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
Complexity:
"""
def convertIncMatrixToList(incMatrix):
	nvertices = incMatrix.nvertices
	nedges = incMatrix.nedges
	newList = adjacencyList(nvertices)

	#
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
			print("error: edge not detected")
		else:
			newList.insertEdge(x,y,True)

"""
TESTS FOR FUNCTIONALITY
"""

if __name__ == "__main__":
	matrix = [ [0] * 5 for _ in range(10)]
	matrix[1][0] = 1
	print(matrix)
