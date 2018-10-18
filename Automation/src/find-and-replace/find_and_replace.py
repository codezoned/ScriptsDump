# Finds and replaces a given string in all the files of a given path.

import os

def input_find():
    print('String do you want to replace: ')
    find = input()
    return find

def input_replace():
    print('String do you want to replace it with: ')
    replace = input()
    return replace

def input_source():
    print('Source of the input files: ')
    source = input()
    return source

def input_destination():
    print('Source of the output files: ')
    destination = input()
    return destination

def find_and_replace():

    find = input_find()
    replace = input_replace()
    source = input_source()
    sourcepath = os.listdir(source)
    destination = input_destination()
    i = 0

    for file in sourcepath:
        inputfile = source + file
        print ('Conversion is ongoing for: ' + inputfile)
        with open(inputfile,'r', encoding='utf-8') as inputfile:
            filedata = inputfile.read()
        destinationpath = destination + file
        filedata = filedata.replace(find, replace)
        with open(destinationpath,'w', encoding='utf-8') as file:
            file.write(filedata)
        i += 1

    print ('Total %d Records Replaced' %i)

find_and_replace()
