from PIL import Image, ImageDraw

im = Image.new(
    "RGBA", (200, 200), "white"
)  # or open an image using "Image.open(in_file)"
draw = ImageDraw.Draw(im)
draw.line(
    [(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill="black"
)  # line(xy, fill, width) for line
draw.rectangle(
    (20, 30, 60, 60), fill="blue"
)  # rectangle(xy, fill, outline) for rectangle
draw.ellipse((120, 30, 160, 60), fill="red")  # ellipse(xy, fill, outline) for ellipse
draw.polygon(
    ((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),  # polygon(xy, fill, outline)
    fill="brown",
)
for i in range(100, 200, 10):
    draw.line([(i, 0), (200, i - 100)], fill="green")
im.save("drawing.png")

