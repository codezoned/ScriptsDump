import os

import shutil

from PIL
import Image

import PIL

import os.path, time

from datetime
import datetime

lis = []

old = ""

new = ""

lis = os.listdir('C:\New folder\\')

lis.sort()

for x in lis:

  if x == __file__:

  continue

if x == 'Thumbs.db':

  continue

print "created: %s" % time.ctime(os.path.getctime(x))

datestring = time.ctime(os.path.getmtime(x))

dt = datetime.strptime(datestring, '%a %b %d %H:%M:%S %Y')

# old = str(dt.month) + '-' + str(dt.day) + '-' + str(dt.year)

#
if old == new:

  #shutil.move(x, destinationDir)

#
else :

  #new = str(dt.month) + '-' + str(dt.day) + '-' + str(dt.year)

destinationDir = 'C:\New folder\\' + str(dt.month) + '-' + str(dt.day) + '-' + str(dt.year)

if not os.path.exists(destinationDir):

  os.makedirs(destinationDir)

shutil.move(x, destinationDir)
