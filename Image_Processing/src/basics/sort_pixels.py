from PIL import Image
import operator


im = Image.open('input.jpg')

width = im.width
height = im.height

sorted_rows = []
for y in range(0, height):
    current_row = []
    for x in range(0, width):
        current_row.append(im.getpixel((x,y)))
    current_row.sort(key = operator.itemgetter(1))
    sorted_rows.append(current_row)

byte_arry = []

for row in sorted_rows:
    for column in row:
        for colour in column:
            byte_arry.append(colour)

sorted_im = Image.new('RGB', (width, height))
sorted_im.frombytes(bytes(byte_arry))
sorted_im.save('output.jpg')
