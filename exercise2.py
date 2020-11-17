from time import process_time_ns
import random

"""
SORTING ALGORITHMS
"""

class selectionSort:
	def sort(self,arr):
		# go through array spot by spot and add to the sorted list
		for i in range(len(arr)):
			min = i
			# find the next lowest value
			for j in range(i+1,len(arr)):
				if arr[j] < arr[min]:
					min = j
			arr[i],arr[min] = arr[min],arr[i]

class insertionSort:
	def sort(self,arr):
		# go through array starting from second pos and insert into sorted list
		for i in range(1,len(arr)):
			j = i
			# if the value should go earlier in the list, swap with previous value
			while j > 0 and arr[j] < arr[j-1]:
				arr[j],arr[j-1] = arr[j-1],arr[j]
				j -= 1

class quickSort:
	def sort(self,arr):
		# do nothing if len(arr) <= 1
		if len(arr) > 1:
			random.shuffle(arr)
			self.quickHelper(arr,0,len(arr)-1)

	def quickHelper(self,arr,low,high):
		if low < high:
			# partition the array with all higher on right side and all lower on left side, with all equal in middle
			#part_left represents leftmost index == partition, part_right represents rightmost ""
			part_left,part_right = self.partition(arr,low,high)
			# sort right side and left side
			if part_right+1 < high:
				self.quickHelper(arr,part_right+1,high)
			if low < part_left-1:
				self.quickHelper(arr,low,part_left-1)

	def partition(self,arr,low,high):
		# choose the last value as partition since values were randomized earlier
		part = arr[high]
		i = low
		j = high - 1

		# swap values to create partition
		while i <= j:
			# move right if not greater than on left
			move_right = arr[i] <= part
			# move left if not less then on right
			move_left = arr[j] >= part
			if move_right:
				i += 1
			if move_left:
				j -= 1
			# if both found values that need switching, then switch
			if not move_right and not move_left:
				arr[i],arr[j] = arr[j],arr[i]
		#switch partition with value on greater side
		arr[i],arr[high] = arr[high],arr[i]
		
		# go through array and move values on the left side that are equal to partition to middle by swapping
		k = low
		next_spot = i
		left_most = i
		while k <= next_spot:
			move_right = arr[k] != part
			move_left = arr[next_spot] == part
			if move_right:
				k += 1
			if move_left:
				next_spot -= 1
			if not move_right and not move_left:
				arr[k],arr[next_spot] = arr[next_spot],arr[k]
				left_most = next_spot
		return left_most,i

class mergeSort:	
	def sort(self,arr):
		# do nothing if len(arr) <= 1
		if len(arr) > 1:
			self.mergeHelper(arr,0,len(arr)-1)

	def mergeHelper(self,arr,low,high):
		if low < high:
			mid = (high-low)//2 + low
			#sort left
			if low < mid:
				self.mergeHelper(arr,low,mid)
			#sort right
			if mid+1 < high:
				self.mergeHelper(arr,mid+1,high)
			#merge sorted right and left
			self.merge(arr,low,mid,high)

	def merge(self,arr,low,mid,high):
		first_queue =[]
		second_queue = []
		#enqueue the values from each half
		for i in range(low,mid+1):
			first_queue.append(arr[i])
		for j in range(mid+1,high+1):
			second_queue.append(arr[j])
		k = low
		#take the lower of each half and insert into the list
		while len(first_queue) != 0 and len(second_queue) != 0:
			if first_queue[0] <= second_queue[0]:
				arr[k] = first_queue.pop(0)
			else:
				arr[k] = second_queue.pop(0)
			k += 1

		#take the leftover values and insert into the list
		while len(first_queue) > 0:
			arr[k] = first_queue.pop(0)
			k += 1
		while len(second_queue) > 0:
			arr[k] = second_queue.pop(0)
			k += 1

class heapSort:
	def sort(self,arr):
		"""
		1. max heapify the array (start at n/2)
		2. repeatedly "remove" the first element and move to end
		idea for bubbledown implementation from https://www.geeksforgeeks.org/heap-sort/
		"""
		self.heapify(arr)
		for i in range(len(arr)-1,0,-1):
			#swap the first and last elements of the heap
			arr[i],arr[0] = arr[0],arr[i]
			self.bubbleDown(arr,0,i)	

	def leftChild(self,i):
		return (2*i) + 1

	def rightChild(self,i):
		return (2*i) + 2

	def heapify(self,arr):
		for i in range(len(arr)//2-1,-1,-1):
			self.bubbleDown(arr,i,len(arr))

	def bubbleDown(self,arr,i,max):
		largest = i
		left = self.leftChild(i)
		right = self.rightChild(i)
		# find which child is largest and bubble down in that direction
		if left < max and arr[left] > arr[largest]:
			largest = left
		if right < max and arr[right] > arr[largest]:
			largest = right
		if largest != i:
			#swap with larger child
			arr[i],arr[largest] = arr[largest],arr[i]
			self.bubbleDown(arr,largest,max)

"""
INSERTING THE WORDS FROM THE FILE
"""

text = []
filepath = 'pride-and-prejudice.txt'
with open(filepath) as fp:
	line = fp.readline()
	word = ''
	while line:
		for i in line:
			if i.isalnum():
				word += i
			else:
				if word:
					text.append(word)
					word = ''
		line = fp.readline()

"""
CREATE 5 NEW ARRAYS FOR DIFF ALGORITHMS TO SORT
"""

test1 = text
test2 = text
test3 = text
test4 = text
test5 = text


"""
SORTING TIME MEASUREMENTS
"""

#MERGESORT
merge = mergeSort()
start = process_time_ns()
merge.sort(test4)
end = process_time_ns()
print("Merge Sort: ", end-start)

#HEAPSORT
heap = heapSort()
start = process_time_ns()
heap.sort(test5)
end = process_time_ns()
print("Heap Sort: ", end-start)


#QUICKSORT
quick = quickSort()
start = process_time_ns()
quick.sort(test3)
end = process_time_ns()
print("Quick Sort: ", end-start)


#SELECTIONSORT
selection = selectionSort()
start = process_time_ns()
selection.sort(test1)
end = process_time_ns()
print("Selection Sort: ", end-start)

#INSERTIONSORT
insertion = insertionSort()
start = process_time_ns()
insertion.sort(test2)
end = process_time_ns()
print("Insertion Sort: ", end-start)

