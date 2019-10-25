#decimal (denary) to hexadecimal converter using ladder method
import math

def denToHex(den):
	result = ""
	hex = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"} #dictionary for quick lookup of hexadecimal values
	
	rem = den % 16					#divide the number by 16 and save the remainder
	quotient = math.floor(den/16)	#rounded down value of number divided by 16
	
	
	while quotient > 0:				#keep going until the quotient is 0
		result = hex[rem]+result	#the hex values are in reverse order
		rem = quotient % 16
		quotient = math.floor(quotient/16)


	result = hex[rem]+result		#adds final hex digit

	return result

print (denToHex(300))				#for testing: denToHex(300) should return 12C