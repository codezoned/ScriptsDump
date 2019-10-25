# Import neccessary libraries
from skimage import io, filters, color


def main(inputfilename, oututfilename):

    # Read image
    img = io.imread(inputfilename)

    # Convert RGB to gray
    img = color.rgb2gray(img)

    # For edge detection
    edge = filters.sobel(img)

    # Display and save image
    io.imshow(edge)
    io.imsave(oututfilename, edge)


if __name__ == "__main__":
    inputfilename = input("Enter a input filename:\t")
    oututfilename = input("Enter a output filename:\t")
    io = main(inputfilename, oututfilename)
