"""
Renames the filenames within the same directory to:
(1) Changes first letter to uppercase
(2) Change the filename to uppercase
(3) Changes the filename to lowercase
Usage:
python treat_names_here.py upper
python treat_names_here.py lower
python treat_names_here.py capitalize
"""

import os
import sys

path =  os.getcwd()
filenames = os.listdir(path)

if(len(sys.argv) > 1):			# check if command-line argument is given
	opt = str(sys.argv[1])
else:			# if not given, print usage
	print("""No command line argument was found
	Usage:
	  python treat_names_here.py upper
	  python treat_names_here.py lower
	  python treat_names_here.py capitalize
	""")
	filenames = ""		# and set filenames to empty string, to bypass for loop

for filename in filenames:
	if filename != os.path.basename(__file__):
		if opt == 'lower':
			os.rename(filename, filename.lower())

		elif opt == 'upper':
			os.rename(filename, filename.upper())
		
		elif opt == 'capitalize':
			os.rename(filename, filename.capitalize())
		
		else:
			print("Unknown argument given")
			break
	else:
		print('omitted actual file')
