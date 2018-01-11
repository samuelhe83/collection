#The simplest sort: The Bubble Sort.
#Time-complexity: W [O(n^2)], Avg [O(n^2)], B [O(n)]

#Notes: This is a poor performance comparative sort under average performance, requiring comparison against each element for each element.  Although it should be noted that if a list is expected to be sorted, it is VERY useful for verifying that.  It is also good for noting how many swaps must be done in order to sort a list (as a general pattern). Best case scenario happens when the list is already sorted.  Average and worst case is everything else.  Frankly, this sort should be avoided UNLESS the list is very small (in favor of the insertion sort).


#Basic iterative in-place Bubblesort with a statemachine to control the while loop.  Easiest version to visualize.
#Note that there are many ways to do this type of implementation, this just happens to be one of the many ways.
def itBsort(some_list): 

	sorted = False
	
	while not sorted:
		sorted = True
		
		for i in range(len(some_list) - 1):
			if some_list[i] < some_list[i + 1]:
				some_list[i], some_list[i + 1] = some_list[i + 1], some_list[i] #Swap.
				sorted = False
				
#I think the various different ways to do this should be discovered by you, because frankly...These are easy.
	


