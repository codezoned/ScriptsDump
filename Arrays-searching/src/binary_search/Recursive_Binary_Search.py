#Recursive Binary search

"""
For this algorithm to work efficiently, it will only have to 
receive a list of numbers previously ordered.
"""

def Recursive_binary_search(vector, start, end, element):
  if len(vector) == 0 and element != "" :
		return "Not found!"
	
	if start <= end:
		mid = (start + end) / 2
		if element > vector[mid]:
			return Recursive_binary_search(vector, mid + 1, end, element)
		elif element < vector[mid]:
			return Recursive_binary_search(vector, start, mid - 1, element)
		else:
			return "Found at!"
	return "Not found!"
