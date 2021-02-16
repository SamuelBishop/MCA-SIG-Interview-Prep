# Was trying to do in an iterative way similar to sol2 without realizing this was the recursion section
def getPermutations1(array):
	output = []
	permutationsHelper1(array, [], output)
	return output
	'''
	Conceptualization of the question:
	- Know we have permuations that start with each number
	- Pick number, remove from list, repeat until we run out of numbers
	- Need a helper method that takes: array, perm, perms
		. If we ever run out of numbers in the list of numbers we have finished
			... Append that permutation to our list of permuations (perms)
		. Else for every number in array
			... newArray = removeNumFrom(array)
				-> To new array that only has corresponding non removed numbers left
			... newPerm = perm + num
			... helper(newArray, newPerm, perms)

	
	- Space and time complexity: (13:27): NEED TO UNDERSTAND THIS
		. How many permutations are there?
			1 - 1
			1, 2 - [1, 2], [2,1]
			1,2,3 - 6
			n! can conceptually arrive at n! n(n-1)(n-2) becomes n!
	'''

def permutationsHelper1(array, remaining, perms):
    if len(array) == 0 and len(remaining):
        perms.append(remaining) # this line will be hit n! times. But how many times will we be calling the helper method
    else:
        for i in range(len(array)): # O(N)
            newArray = array[:i] + array[i + 1 :] # Grab everything until i and leave out i and grab everything after that. Take out I but leave everythine else in
			# WHY? Do on paper for better understanding
			# This is O(N)
			
            newPerm = remaining + [array[i]] # Need to understand this line well as well
			# Transferring the data here is also an O(N) operation
            permutationsHelper1(newArray, newPerm, perms)
			# can build tree to determine that we make n! * n calls to the helper method
			
# Break it down: O(N) operation and O(N!) operation happens O(N) times Meaning this is O(N * N *N!) or simly O(N^2 * N!)
# Space: O(N! * N) where N! is the number of permutations and each permutation is length N




def getPermutations2(array):
	'''
	Now there is a better way to do what we just did then:
	- Pretty similar with just a slight twist
		. Do we actually have to create all of these new arrays every time?
		. That is where a lot of the complexity went
	- There is a way to do this while having everything in place
	- We will build all of the permutations for this array in this array
	
	PSUEDOCODE:
	1. Create pointers to all n elements in array?
	2. Need a swap function
	3. Swap through all of the numbers and swap within those so you will everything within the first number
	4. Super confusing and non intuitive way of solving this problem
	
	helper(i, array, permutations):
		if i last position:
			perms.append(copy of array)
		else:
			for i from i to end of array:
				swap(i, j) # swap i and j
				helper(i + 1, array, perms) # The concept is that instead of taking an interger out of the generated array you just swap until the position you need
				swap(i, j) # swap back
	'''
	permutations = []
	permutationsHelper2(0, array, permutations)
	return permutations

def permutationsHelper2(i, array, permutations):
	if i == len(array) - 1:
		permutations.append(array[:])
	else:
		for j in range(i, len(array)):
			swap(array, i, j)
			permutationsHelper2(i + 1, array, permutations)
			swap(array, i, j)
			
def swap(array, i, j):
	array[i], array[j] = array[j], array[i]



array = [1,2,3]
print(getPermutations1(array))
print(getPermutations2(array))