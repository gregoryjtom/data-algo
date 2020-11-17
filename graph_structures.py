
#graph_structures.py

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
		#check for errors
		"""
		FOR NUMBERING 0 through nvertices-1
		if x < 0 or x > self.nvertices-1 or y < 0 or y > self.nvertices-1:
			print("Vertices out of bounds.")
			return
		"""
		#For starting with A:
		i = ord(x)-ord('A')
		curr = self.edges[i]
		while curr is not None:
			if curr.vertex == y:
				print("Edge already in list.")
				return
			curr = curr.next
		#create new node and set next to the existing list of nodes
		newEdge = self.edgeNode(y)
		newEdge.next = self.edges[i]
		self.edges[i] = newEdge
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
		if x < 0 or x > self.nvertices-1 or y < 0 or y > self.nvertices-1:
			print("Vertices out of bounds.")
			return
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
		if x < 0 or x > self.nvertices-1 or y < 0 or y > self.nvertices-1:
			print("Vertices out of bounds.")
			return
		if self.nextEdge+1 > self.nedges:
			print("More edges than declared.")
			return
		#change the correct vertices to 1 to indicate an edge
		self.matrix[x][self.nextEdge] = 1
		self.matrix[y][self.nextEdge] = 1
		#increment the counter
		self.nextEdge += 1
