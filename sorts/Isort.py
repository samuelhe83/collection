#Simple Sort #3: The Insertion Sort.
#Time-complexity: W [O(n^2)], Avg [O(n^2)], B [O(n)],

#Notes: While this sort does share the same time-complexities as bubble sort, it has some very unique attributes that make it actually useful (lol).  The Worst case for this algorithm is an already-sorted-reversed list.  The Best case for this algorithm is when the list is already sorted (just like bubble sort).  The average case is anything inbetween those two.  It should be noted that the Avg case time complexity is still quadratic (n^2), so this REALLY shouldn't be used on large lists. As I stated, there are some advantages over bubblesort that are notable: It's adaptive (good for "partially-sorted" lists) and it's reactive [Online] (it can insert newly crafted elements right into its sorting pattern, thus allowing it to be ran on a stream of incoming things).

#The idea: Start at the left hand side (recursion works in "reverse"), with our right_bound increasing "slicing" our list into small parts.  Slide our right_bound toward the left until we identify where it needs to be inserted, and then swap.  Then we increase our right_bound by 1 and do it again, and again, and again, and again, until the list is sorted.

#Simple recursive in-place insertion sort.
def Isort(some_list, right_idx):
	if right_idx:
		right_val = some_list[right_idx]
		right_idx -= 1
		
		Isort(some_list, right_idx)
		
		while right_idx >= 0 and some_list[right_idx] > right_val: #Sliding pointer and swap all the way to the left.
			
			some_list[right_idx + 1] = some_list[right_idx]
			right_idx -= 1
			
		some_list[right_idx + 1] = right_val
		
		
#For the iterative version, since we don't have a nice reduction-way to control our right_bound like recursion, we start at the left with our right-bound increasing effectively "slicing" our list.  Then we perform the same idea: slide our pointer to the left and insert our value where it needs to go.
#Simple iterative in-place insertion sort.
def itIsort(some_list):
		
	right_bound = len(some_list)
	
	for idx in range(1, right_bound):
		insertion_val = some_list[idx]
		
		while idx > 0 and some_list[idx - 1] > insertion_val:
		
			some_list[idx] = some_list[idx - 1]
			idx -= 1
		
		
		some_list[idx] = insertion_val


		
		
		
		