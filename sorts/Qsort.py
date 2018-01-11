#The Quicksort.
#Time-complexity: W [O(n^2)], Avg [O(n * log(n))], B [O(n * log(n))]

#Notes: This is a relatively high performance comparative sort that performs well for an average case scenario (some duplicates in list).  Its worst case scenario is when there are absolutely no duplicates in the list, which will require comparison against each element for each element (producing a time complexity of O(n^2)).

#This sort comes in two varities:
	#The in-place sorts:
		#These sorts consists of two parts (each):
			#1. The Driver (Qsort/itQsort) function.
			#2. The helper (partition/partition2) function.
	#The out-of-place sort:
		#Does not use a helper function
		#Uses lots of memory as it creates a duplicate of list (definition of out-of-place).

		
		
#The easiest, but most memory-intensive/slow version of Qsort (NOT an in-place sort).  Frankly, if you need an out-of-place iterative (non-recursive) Qsort, you're better off copying your list initially, and then using the in-place iterative quicksort found later in this script (itQsort).
def easyQsort(some_list):
	
	if len(some_list) < 2:
		return some_list
	else:
		pivot = some_list[0]
		
		less = []
		equals = []
		greater = []

		for num in some_list:
			if num < pivot:
				less.append(num)
			elif num > pivot:
				greater.append(num)
			else:
				equals.append(num)
				
		return easyQsort(less) + equals + easyQsort(greater)




#Pointer-partition.		
def partition(some_list, left_idx, right_idx):

	pivot_value = some_list[left_idx]
	orig_pivot_idx = left_idx
	
	left_idx += 1 #To shift "over" the pivot_value idx
	
	
	while True:
		while left_idx <= right_idx and  some_list[left_idx] <= pivot_value: #Slide the left pointer
			left_idx += 1
		while right_idx >= left_idx and some_list[right_idx] >= pivot_value: #Slide the right pointer
			right_idx -= 1
			
		if left_idx >= right_idx: #Break if the left passed/is equal to the right.
			break
		
		some_list[left_idx], some_list[right_idx] = some_list[right_idx], some_list[left_idx] #Swap.

	#After all of them have been swapped, swap the pivot to the "ending" (right-most) location.
	some_list[orig_pivot_idx], some_list[right_idx] = some_list[right_idx], some_list[orig_pivot_idx]
	
	return right_idx

#For loop partition.	
def partition2(some_list, left_idx, right_idx):
	pivot_val = some_list[right_idx] #Note, this one uses the RIGHT-MOST IDX for pivot.  It's totally possible to make this work just like the other partition using the left-most idx as the pivot, but I thought it'd be fun to show you that you can do it both ways.
	ending_idx = left_idx
	
	for i in range(left_idx, right_idx):
		
		if some_list[i] <= pivot_val:
			some_list[ending_idx], some_list[i] = some_list[i], some_list[ending_idx] #Swap, important to swap here BEFORE incrementing the ending_idx.
			ending_idx += 1

	#After all of them have been swapped, swap the pivot to the "ending" just like the other partition.
	some_list[ending_idx], some_list[right_idx] = some_list[right_idx], some_list[ending_idx]
	
	return ending_idx
	
	
#You can use either partition in either method, and it'll work just fine.

#Basic recursive Qsort.
def Qsort(some_list, left_idx, right_idx):

	if left_idx >= right_idx:
		return None #Just need it to stop recursing, since all the swaps are done in-place.
	else:
		piv_idx = partition2(some_list, left_idx, right_idx)
		
		Qsort(some_list, left_idx, piv_idx - 1)
		Qsort(some_list, piv_idx + 1, right_idx)

#Iterative Qsort with a stack.  In this version, we use the stack to hold our "right/left" of pivots, and then pop them off in pairs, re-partition, push again (if necessary to be repartitioned), pop off in pairs, repartition, repeat until it's no longer necessary.
def itQsort(some_list, left_idx, right_idx):
	stack = [] #makeshift "stack", just using append for push and pop for pop.
	
	stack.append(left_idx)
	stack.append(right_idx)
	
	while len(stack) >= 2: #2 Because there's already 2 things in the stack, and if it ever falls below that, then we know neither if conditional ran and the list is sorted.
		right_idx = stack.pop()
		left_idx = stack.pop()

		pivot_idx = partition2(some_list, left_idx, right_idx) #Just like in the recursive Qsort before, our partition function is doing most of the actual sorting work.
		
		if pivot_idx - 1 > left_idx: #Necessary condition for re-partition left-side.
			stack.append(left_idx)
			stack.append(pivot_idx - 1)


		if pivot_idx + 1 < right_idx: #Necessary condition for re-partition right-side.
			stack.append(pivot_idx + 1)
			stack.append(right_idx)
	
	
	

if __name__ == '__main__':
	import random
	import time

	a = [random.randint(0, 200000) for x in xrange(200000)] #200,000 length list of integers.
	b = [x for x in a] #Hard copy.
	c = [x for x in a] #Hard copy.
	print "Done generating lists."
	print "-" * 50

	start = time.time()
	print "Starting built-in tim sort."
	a.sort()
	print "Done with built-in tim sort.  Took: {} seconds. :C Using C is cheating.".format(time.time() - start)
	print "-" * 50

	start = time.time()
	print "Starting recursive Qsort."
	Qsort(b, 0, len(b) - 1)
	print "Done with recursive Qsort.  Took: {} seconds.".format(time.time() - start)
	print "-" * 50

	start = time.time()
	print "Starting iterative Qsort."
	itQsort(c, 0, len(b) - 1)
	print "Done with iterative Qsort.  Took: {} seconds.".format(time.time() - start)
	print "-" * 50

	print "Truthiness check to see if all arrays are equal: {}".format(a == b == c)

	
		

