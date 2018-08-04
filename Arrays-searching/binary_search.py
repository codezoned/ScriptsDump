"""
   Written By @searpheon - Arka
   BINARY SEARCH
"""

def binary_search(item_list,item): //creating the function
	first = 0 //first element
	last = len(item_list)-1 //self explanatory
	found = False //setting value top false if we find the element we are looking for
	while( first<=last and not found):
		mid = (first + last)//setting value of middle element
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1 //shifting middle element's subset to the left
			else:
				first = mid + 1	//" " " " to the right
	return found

print(binary_search([1,2,3,5,8], 6))
print(binary_search([1,2,3,5,8], 5))
