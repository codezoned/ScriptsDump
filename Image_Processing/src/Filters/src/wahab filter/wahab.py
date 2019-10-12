#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from optparse import OptionParser
import scipy.misc as misc
import scipy.ndimage as ndimage
from skimage import draw

import utils
from utils import showImage

parser = OptionParser(usage="%prog [options] sourceimage [destinationimage]")

parser.add_option("-i", dest="images", default=0, action="count",
        help="Show intermediate images.")

parser.add_option("-d", "--dry-run", dest="dryrun", default=False, action="store_true",
        help="Do not save the result.")

parser.add_option("-b", "--no-binarization", dest="binarize", default=True, action="store_false",
        help="Use this option to disable the final binarization step")

(options, args) = parser.parse_args()

if len(args) == 0 or len(args) > 2:
    parser.print_help()
    exit(1)

sourceImage = args[0]
if len(args) == 1:
    destinationImage = args[0]
else:
    destinationImage = args[1]

def wahabKernel(size, angle):
    y = int(np.sin(angle) * size)
    x = int(np.cos(angle) * size)

    kernel = np.zeros((np.abs(y) + 1, np.abs(x) + 1))

    if y < 0:
        rr, cc = draw.line(0, 0, y, x)
    else:
        rr, cc = draw.line(-y, 0, 0, x)

    kernel[rr, cc] = 1.0
    return kernel


def wahabFilter(image, orientations, w=8):
    result = np.empty(image.shape)

    height, width = image.shape
    for y in range(0, height - w, w):
        for x in range(0, width - w, w):
            orientation = orientations[y+w//2, x+w//2]
            kernel = wahabKernel(16, orientation)
            result[y:y+w, x:x+w] = utils.convolve(image, kernel, (y, x), (w, w))
            result[y:y+w, x:x+w] /= np.sum(kernel)

    return result


if __name__ == '__main__':
    np.set_printoptions(
            threshold=np.inf,
            precision=4,
            suppress=True)

    print("Reading image")
    image = ndimage.imread(sourceImage, mode="L").astype("float64")
    if options.images > 0:
        utils.showImage(image, "original", vmax=255.0)

    print("Normalizing")
    image = utils.normalize(image)
    if options.images > 1:
        utils.showImage(image, "normalized")

    print("Finding mask")
    mask = utils.findMask(image)
    if options.images > 1:
        utils.showImage(mask, "mask")

    print("Applying local normalization")
    image = np.where(mask == 1.0, utils.localNormalize(image), image)
    if options.images > 1:
        utils.showImage(image, "locally normalized")

    print("Estimating orientations")
    orientations = np.where(mask == 1.0, utils.estimateOrientations(image, interpolate=False), -1.0)
    if options.images > 0:
        utils.showOrientations(image, orientations, "orientations", 8)

    print("Filtering")
    image = np.where(mask == 1.0, wahabFilter(image, orientations), 1.0)
    if options.images > 0:
        utils.showImage(image, "filtered")

    if options.binarize:
        print("Binarizing")
        image = np.where(mask == 1.0, utils.binarize(image), 1.0)
        if options.images > 0:
            utils.showImage(image, "binarized")

    if options.images > 0:
        plt.show()

    if not options.dryrun:
        misc.imsave(destinationImage, image)