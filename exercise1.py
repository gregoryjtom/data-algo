from time import process_time_ns

"""
DATA STRUCTURE IMPLEMENTATION
"""

#LINKEDLIST

class LLNode:
	def __init__(self,value = None):
		self.val = value
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def contains(self,value):
		curr = self.head
		# go to the end of the linked list and compare every node to the search value
		while curr is not None:
			if curr.val == value:
				return True
			curr = curr.next
		return False

	def add(self,input):
		#check if list contains the input
		if self.contains(input):
			return False
		#create new node and add to the linked list
		next = self.head
		new = LLNode(input)
		new.next = next
		self.head = new
		self.size += 1
		return True

	def size(self):
		return self.size

#BINARYTREE

class BTNode:
	def __init__(self,value = None):
		self.val = value
		self.left = None
		self.right = None

	def search(self,value,add):
		#boolean add tells whether to add a node if one does not exist, or just to return
		#if the head value has no value yet:
		if self.val is None:
			if add:
				self.val = value
			return False
		#if current node equals value
		if value == self.val:
			return True
		elif value < self.val:
			if self.left is None:
				#add a new node if necessary
				if add:
					self.left = BTNode(value)
				return False
			return self.left.search(value,add)
		else:
			if self.right is None:
				#add a new node if necessary
				if add:
					self.right = BTNode(value)
				return False 
			return self.right.search(value,add)

	def contains(self,value):
		if self.search(value,False):
			return True
		return False

	def add(self,input):	
		if self.search(input,True):
			return False
		return True

#class that uses BTNode and stores size
class BinaryTree:
	def __init__(self):
		self.head = BTNode()
		self.size = 0

	def add(self,input):
		if self.head.add(input):
			self.size += 1
			return True
		return False

	def contains(self,value):
		if self.head.contains(value):
			return True
		return False

	def size(self):
		return self.size

#HASHTABLE

class HashTable:
	def __init__(self,buckets = 100):
		self.table = [LinkedList()] * 8192 #initialize with 8192 buckets, this can be changed
		self.size = 0

	def hasher(self,value):
		#add each character of the string together, multiplying each ord() value by 60^(index+1)
		#idea from https://cp-algorithms.com/string/string-hashing.html
		hash_value = 0
		power = 0
		n = 60
		for i in value:
			hash_value += ord(i)*(n**power)
			power += 1
		return hash_value % 8192


	def add(self,input):
		hash_value = self.hasher(input)
		#add to linked list at hash bucket
		if self.table[hash_value].add(input):
			self.size += 1
			return True
		return False

	def contains(self,value):
		hash_value = self.hasher(value)
		#check linked list at hash bucket
		if self.table[hash_value].contains(value):
			return True
		return False

	def size(self,value):
		return self.size

"""
TESTING DATA STRUCTURES
"""

#INSERTING

# NOTE: replacing set_structure = BinaryTree() with LinkedList() or HashTable() gives the other times.
print("ADDING")
set_structure = BinaryTree()
filepath = 'pride-and-prejudice.txt'
with open(filepath) as fp:
	line = fp.readline()
	word = ''
	#read line by line
	while line:
		for i in line:
			#if alphanumeric character, add to existing word
			if i.isalnum():
				word += i
			#if not alphanumeric character, then try to insert existing word
			else:
				if word:
					start = process_time_ns()
					success = set_structure.add(word)
					end = process_time_ns()
					#only print the adding time if adding was successful
					if success:
						print(set_structure.size-1,end - start)
					word = ''
		line = fp.readline()

print("The number of words in the set is " + str(set_structure.size) + ".")

#SEARCHING

print("SEARCHING")
filepath = 'words-shuffled.txt'
#count of words not in the above text
count = 0
with open(filepath) as fp:
	line = fp.readline()
	word = ''
	while line:
		for i in line:
			if i.isalnum():
				word += i
			else:
				if word:
					start = process_time_ns()
					success = set_structure.contains(word)
					end = process_time_ns()
					print(end-start)
					#if the structure did not contain the word, add one to count
					if not success:
						count += 1
					word = ''
		line = fp.readline()
print("After search, the number of words not in the set is " + str(count) + ".")









