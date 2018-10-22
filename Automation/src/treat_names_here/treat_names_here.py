import os
import sys

""" 
Renames the filenames within the same directory to:
(1) Changes first letter to uppercase
(2) Change the filename to uppercase
(3) Changes the filename to lowercase
Usage:
python upper treat_names_here.py
python lower treat_names_here.py
python capitalize treat_names_here.py
"""

path =  os.getcwd()
filenames = os.listdir(path)
opt = str(sys.argv[1])

for filename in filenames:
	if filename != os.path.basename(__file__):
		if opt == 'lower':
			os.rename(filename, filename.lower())

		if opt == 'upper':
			os.rename(filename, filename.upper())
		
		if opt == 'capitalize':
			os.rename(filename, filename.capitalize())
	else:
		print('omitted actual file')