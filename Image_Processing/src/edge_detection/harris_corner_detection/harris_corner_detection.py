# Import necessary libararies
from matplotlib import pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.feature import corner_harris, corner_subpix, corner_peaks


def main(inputfilename, oututfilename):
    # Load image
    image = imread(inputfilename)
    image = rgb2gray(image)

    # Apply corner detection algorithm
    corners = corner_harris(image)
    coords = corner_peaks(corners, min_distance=5)
    coords_subpix = corner_subpix(image, coords, window_size=13)

    # Diplay the image
    fig, ax = plt.subplots()
    ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
    ax.plot(coords[:, 1], coords[:, 0], '.b', markersize=3)
    ax.plot(coords_subpix[:, 1], coords_subpix[:, 0], '+r', markersize=15)
    ax.axis((0, 350, 350, 0))
    plt.savefig(oututfilename)


if __name__ == "__main__":
    inputfilename = input("Enter a input filename:\t")
    oututfilename = input("Enter a output filename:\t")
    main(inputfilename, oututfilename)
