"""
	Written By @searpheon - Arka
	Updated By @nishantcoder97 - Nishant Nahata
	BINARY SEARCH
"""

"""
	Condition: List should be sorted in ascending order
"""
def binary_search(item_list, item):
	"""
	param: list item_list: List to be searched
	param: int item: Item to be searched for
	returns: int index: Index of the first occurrence of item, or len(tem_list) if not found
	"""
	first = 0
	last = len(item_list)-1 
	index = len(item_list)
	while first < last:
		mid = int((first + last) / 2)
		if item_list[mid] >= item:
			last = mid
		else:
			first = mid + 1
	if item_list[first] == item:
		index = first
	return index


if __name__ == '__main__':
	   ### Tests ###
	print(binary_search([1,2,3,5,8], 6)) # returns len(item_list)
	print(binary_search([1,2,3,5,8], 5)) # returns 3
	print(binary_search([1, 2, 3, 3, 3, 4, 4, 5, 10], 4)) # returns 5


