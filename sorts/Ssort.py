#Simple sort #2: The Selection Sort.
#Time-complexity: W [O(n^2)], Avg [O(n^2)], B [O(n^2)]

#Notes:  While I absolutely detest this sorts time complexities, it is the first simple sort that implements an idea of sliding around pointers to find something (a very important concept in all of the later comparative sorts) and to swap more than just elements "next-to-eachother".  While the variance of actual speed is influenced by the initial order of the array, there is no time-complexity distinguishment to discuss between W/Avg/B scenarios.  Frankly, this sort is slow as hell (just like bubble sort) and shouldn't really be used unless you need an in-place sieving-type technique (honestly, I can't even think of an applicable scenario, nor do I know why I know this sort other than conceptually).


#Recursive Selection Sort, uses a helper function called find_min because...lazy.
def Ssort(some_list, size, left_idx):
	
	if size == left_idx:
		return
	else:
		
		min_idx = find_min(some_list, left_idx)
		
		if min_idx != left_idx:
			some_list[min_idx], some_list[left_idx] = some_list[left_idx], some_list[min_idx]
			
		
		Ssort(some_list, size, left_idx + 1)
	
def find_min(some_list, left_idx): #Helper function, finds min.
	min_idx = left_idx
	
	for idx in range(left_idx + 1, len(some_list)):
		if some_list[idx] < some_list[min_idx]:
			min_idx = idx
			
	return min_idx


#A basic iterative selection sort:
def itSsort(some_list):
	right_bound = len(some_list)
	
	for idx in range(len(some_list)):
		idx_min = idx #Assume that we have the least.
		
		#Scroll through the list to find the real minimum.
		for compare in range(idx + 1, len(some_list)):
			if some_list[compare] < some_list[idx_min]:
				idx_min = compare
				
		
		if idx_min != idx: #If our starting "minimum" isn't actually the minimum...
			some_list[idx_min], some_list[idx] = some_list[idx], some_list[idx_min] #Swap.

			


