# Validating JSON using Phython Code
import json,os,sys
import csv
import ast
from jsonschema import validate


def json_validator(data):
    try:
        json.loads(data)
        return True
    except ValueError as error:
        print("invalid json: %s" % error)
        return False





def check_all_json_files(path):

	file_names = os.listdir(path)

	for file_name in file_names:
		if(file_name.endswith('.json')):
			f=open(os.path.join(path,file_name))
			content = f.read()
			if(json_validator(content)):
				print("Vald json of file " + file_name)
			else:
				print("Vald json of file " + file_name)



if __name__ == "__main__":

	if(len(sys.argv)!=2):
		print("Invalid number of Arguments")
		raise SystemExit
	else:
		path = sys.argv[1]
		check_all_json_files(path)

