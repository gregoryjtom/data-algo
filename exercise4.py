"""
NOTES:
outline of file:
1) function to construct graph A using adjacency list
2) functions for algorithms
	a) BFS
	b) DFS

- assumption: the whole graph is connected (as the graphs in the textbook are)
- other note: used inspiration from textbook BFS and DFS algorithms
"""

"""
INITIALIZING GRAPHS
"""
#import adjacencyList from exercise 3 code
from graph_structures import adjacencyList

def initializeA():
	graphA = adjacencyList(10)
	#vertex A
	graphA.insertEdge('A','B',True)
	graphA.insertEdge('A','D',True)
	graphA.insertEdge('A','I',True)
	#vertex B
	graphA.insertEdge('B','D',True)
	graphA.insertEdge('B','E',True)
	graphA.insertEdge('B','C',True)
	#vertex C
	graphA.insertEdge('C','E',True)
	graphA.insertEdge('C','F',True)
	#vertex D
	graphA.insertEdge('D','E',True)
	graphA.insertEdge('D','G',True)
	#vertex E
	graphA.insertEdge('E','F',True)
	graphA.insertEdge('E','G',True)
	graphA.insertEdge('E','H',True)
	#vertex F
	graphA.insertEdge('F','H',True)
	#vertex G
	graphA.insertEdge('G','H',True)
	graphA.insertEdge('G','I',True)
	graphA.insertEdge('G','J',True)
	#vertex H
	graphA.insertEdge('H','J',True)
	#vertex I/J
	graphA.insertEdge('J','I',True)
	return graphA

"""
SEARCH ALGORITHMS
"""
def BFS(graph,start):
	#initialize discovered array, queue
	n = graph.nvertices
	discovered = [0] * n
	queue = []

	#start with the first vertex and add to queue
	ind_start = ord(start) - ord('A')
	queue.append(start)
	discovered[ind_start] = 1

	#process each vertex one by one, breadth first search style by popping off queue
	while len(queue) > 0:
		v = queue.pop(0)
		#print the current vertex being processed and calculate index
		print(v)
		ind_v = ord(v) - ord('A')

		#loop through all the adjacencies in the vertex, adding each one to next_vertices
		next_vertices = []
		curr = graph.edges[ind_v]
		while curr is not None:
			p = curr.vertex
			ind_p = ord(p) - ord('A')
			if not discovered[ind_p]:
				discovered[ind_p] = 1
				next_vertices.append(p)
			curr = curr.next

		#sort the adjacencies, then add to queue, lowest alphabetical first
		next_vertices.sort()
		while len(next_vertices) > 0:
			i = next_vertices.pop(0)
			queue.append(i)

def DFS(graph,start):
	#initialize processed array, stack
	n = graph.nvertices
	processed = [0] * n
	stack = []

	#start with the first vertex and add to stack
	ind_start = ord(start) - ord('A')
	stack.append(start)

	#process each vertex one by one, depth first search style by popping off stack
	while len(stack) > 0:
		v = stack.pop()
		ind_v = ord(v) - ord('A')
		#if processed already, then skip this vertex
		if not processed[ind_v]:
			#print the current vertex being processed
			print(v)
			#loop through all the adjacencies in the vertex, adding each one to next_vertices
			next_vertices = []
			curr = graph.edges[ind_v]
			while curr is not None:
				p = curr.vertex
				ind_p = ord(p) - ord('A')
				if not processed[ind_p]:
					next_vertices.append(p)
				curr = curr.next

			#sort the adjacencies, then add to stack, highest alphabetical first, so lowest goes first
			next_vertices.sort()
			while len(next_vertices) > 0:
				i = next_vertices.pop()
				stack.append(i)

			#mark the vertex as processed
			processed[ind_v] = 1


if __name__ == "__main__":
	graphA = initializeA()
	print("BREADTH FIRST SEARCH:")
	BFS(graphA,'A')
	print("DEPTH FIRST SEARCH:")
	DFS(graphA,'F')


	