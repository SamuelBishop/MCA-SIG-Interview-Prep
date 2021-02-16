# Classic recursive function example
# This is O(N^2) time (because the function runs twice) and O(N) space on the stack
def getNthFib1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    return getNthFib1(n - 1) + getNthFib1(n - 2)

# Recursive functions using a hashtable to speed up time complexity
# O(N) time and O(N) space
def getNthFib2(n, hashMap = {1:0, 2:1}):
	if n in hashMap:
		return hashMap[n]
	else:
		hashMap[n] = getNthFib2(n - 1, hashMap) + getNthFib2(n - 2, hashMap)
	return hashMap[n]


# Iterative way (Not what we were going for this meeting)
# O(N) time and O(1) space
def getNthFib3(n):
    array = [0, 1]
    counter = 3
    while counter <= n:
        temp = array[0] + array[1]
        array[0] = array[1]
        array[1] = temp
        counter += 1
    return array[1] if n > 1 else array[0]

print(getNthFib1(8))
print(getNthFib2(7))
print(getNthFib3(6))