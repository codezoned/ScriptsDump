__author__ = 'Tania Reyes - reyes.mtz.tania@gmail.com'
# for more information about this script please visit https://github.com/taniaReyesM/color_cloth
"""
color_cloth gets the main colors and its proportions from a cloth image using the EM algorithm from OpenCV library,
it assumes that the item is in the center of the image.
"""

import math
import numpy as np
import cv2
import sys


def get_hue(a, b):
    if a == 0 or b == 0:
        h = 0
    else:
        h = math.atan2(b, a)
        h = (h / math.pi) * 180
    return h


def CIE2000_distance(lab1, lab2):
    # formula from: http://www.ece.rochester.edu/~gsharma/papers/CIEDE2000CRNAFeb05.pdf

    lab1 = [lab1[0] / 255 * 100.0, lab1[1] - 128, lab1[2] - 128]
    lab2 = [lab2[0] / 255 * 100.0, lab2[1] - 128, lab2[2] - 128]

    c1 = math.sqrt(lab1[1] ** 2 + lab1[2] ** 2)
    c2 = math.sqrt(lab2[1] ** 2 + lab2[2] ** 2)

    c_mean = (c1 + c2) / 2.0

    G = 0.5 * (1 - math.sqrt(c_mean ** 7 / float(c_mean ** 7 + 25 ** 7)))

    a_1 = (1 + G) * lab1[1]
    a_2 = (1 + G) * lab2[1]

    C_prime_1 = math.sqrt(a_1 ** 2 + lab1[2] ** 2)
    C_prime_2 = math.sqrt(a_2 ** 2 + lab2[2] ** 2)

    h_1 = get_hue(a_1, lab1[2])
    h_2 = get_hue(a_2, lab2[2])

    delta_L = lab2[0] - lab1[0]
    delta_C = C_prime_2 - C_prime_1

    if C_prime_1 * C_prime_2 == 0:
        delta_h = 0
    else:
        if abs(h_2 - h_1) <= 180:
            delta_h = h_2 - h_1
        elif h_2 - h_1 > 180:
            delta_h = h_2 - h_1 - 360
        else:
            delta_h = h_2 - h_1 + 360

    delta_H = 2 * math.sqrt(c1 * c2) * math.sin(delta_h * math.pi / 2.0 * 180)

    l_mean = (lab1[0] + lab2[0]) / 2.0
    c_prime_mean = (C_prime_1 + C_prime_2) / 2.0

    if C_prime_1 * C_prime_2 == 0:
        h_mean = h_1 + h_2
    else:
        if abs(h_1 - h_2) <= 180:
            h_mean = (h_1 + h_2) / 2.0
        else:
            if h_1 + h_2 < 360:
                h_mean = (h_1 + h_2 + 360) / 2.0
            else:
                h_mean = (h_1 + h_2 - 360) / 2.0

    T = 1 - 0.17 * math.cos((h_mean - 30) * math.pi / 180.0) \
        + 0.24 * math.cos(2 * h_mean * math.pi / 180.0) \
        + 0.32 * math.cos((3 * h_mean + 6) * math.pi / 180.0) \
        - 0.2 * math.cos((4 * h_mean - 63) * math.pi / 180.0)

    delta_Phi = 30 * math.exp(-((h_mean - 275) / 25.0) ** 2)
    R_c = 2 * math.sqrt(c_prime_mean ** 7 / float(c_prime_mean ** 7 + 25 ** 7))
    S_l = 1 + (0.015 * (l_mean - 50) ** 2) / math.sqrt(20 + (l_mean - 50) ** 2)
    S_c = 1 + 0.045 * c_prime_mean
    S_h = 1 + 0.015 * c_prime_mean * T
    R_t = -math.sin(2 * delta_Phi * math.pi / 180.0) * R_c

    distance = math.sqrt((delta_L / S_l) ** 2
                         + (delta_C / S_c) ** 2
                         + (delta_H / S_h) ** 2
                         + R_t * (delta_C / S_c) * (delta_H / S_h))
    return distance


def LAB_shadow(LAB_color_1, LAB_color_2):

    #when a color is darker the values in A and B remains almost the same
    #but the value in Lightness changes more

    threshold_L = 70
    threshold_A = 15
    threshold_B = 20

    distance_in_L = math.fabs(LAB_color_1[0] - LAB_color_2[0])
    distance_in_A = math.fabs(LAB_color_1[1] - LAB_color_2[1])
    distance_in_B = math.fabs(LAB_color_1[2] - LAB_color_2[2])

    if distance_in_L < threshold_L \
            and distance_in_A < threshold_A \
            and distance_in_B < threshold_B:
        return True

    return False


def cloth_color(image_path, expected_size=40, in_clusters=7, out_clusters=3, final_size=300):

    initial_image = cv2.imread(image_path)

    if initial_image is not None:
        height, width = initial_image.shape[:2]

        factor = math.sqrt(width * height / (expected_size * expected_size))

        #image downsample
        image = cv2.resize(initial_image,
                           (int(width / factor), int(height / factor)),
                           interpolation=cv2.INTER_LINEAR)

        LAB_image = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
        frame_width = int(expected_size / 10 + 2)
        in_samples = []

        border_samples = []

        limit_Y = LAB_image.shape[0] - frame_width
        limit_X = LAB_image.shape[1] - frame_width

        for y in range(LAB_image.shape[0] - 1):
            for x in range(LAB_image.shape[1] - 1):
                pt = LAB_image[y][x]
                if x < frame_width or y < frame_width or y >= limit_Y or x >= limit_X:
                    border_samples.append(pt)
                else:
                    in_samples.append(pt)

        in_samples = np.array(in_samples, dtype=float)
        border_samples = np.array(border_samples, dtype=float)

        em_in = cv2.ml.EM_create()
        em_in.setClustersNumber(in_clusters)
        in_etval, in_likelihoods, in_labels, in_probs = em_in.trainEM(in_samples)

        in_means = em_in.getMeans()
        in_covs = em_in.getCovs()

        em_border = cv2.ml.EM_create()
        em_border.setClustersNumber(out_clusters)
        border_etval, border_likelihoods, border_labels, border_probs = em_border.trainEM(border_samples)

        border_means = em_border.getMeans()

        unique_border, counts_border = np.unique(border_labels, return_counts=True)
        count_border_labels = dict(zip(unique_border, counts_border))

        unique, counts = np.unique(in_labels, return_counts=True)

        count_in_labels = dict(zip(unique, counts))
        in_len = len(in_covs)

        valid = [True] * in_len

        # colors vs background
        for i in range(in_len):
            if not valid[i]:
                continue

            prop_in = float(count_in_labels[i]) / len(in_labels)

            #if the proportion is too small can be only buttons or labels
            if prop_in < 0.05:
                valid[i] = False
                continue

            # remove similar colors
            for key in count_border_labels:
                prop_border = float(count_border_labels[key]) / len(border_labels)

                #if the color appears more in the center, it belongs to the cloth
                #else is background
                if prop_in > prop_border:
                    continue

                cie_dst = CIE2000_distance(in_means[i], border_means[key])

                if cie_dst < 5:
                    valid[i] = False

        # colors vs colors
        for i in range(in_len):
            if not valid[i]:
                continue

            for j in range(i + 1, in_len):
                if not valid[j]:
                    continue

                #removes shadows and similar colors
                cie_dst = CIE2000_distance(in_means[i], in_means[j])

                is_shadow = LAB_shadow(in_means[i], in_means[j])

                if is_shadow or cie_dst < 20:
                    if count_in_labels[j] > count_in_labels[i]:
                        valid[i] = False

                        count_in_labels[j] += count_in_labels[i]
                        break
                    else:
                        valid[j] = False
                        count_in_labels[i] += count_in_labels[j]

        num_valid = sum(True == x for x in valid)

        colors = []
        proportions = []
        total_color = 0

        #if the cloth is of the same color that the background, takes the more common color
        if num_valid == 0:
            pos = max(count_in_labels, key=count_in_labels.get)
            colors = [in_means[pos]]
            proportions = [count_in_labels[pos]]
            total_color = count_in_labels[pos]

        for i in range(in_len):

            if not valid[i]:
                continue

            color = in_means[i]
            quantity = count_in_labels[i]
            colors.append(color)
            proportions.append(quantity)
            total_color += quantity

        factor = max(1,math.sqrt(width * height / (final_size * final_size)))

        final_image = cv2.resize(initial_image,
                                 (int(width / factor),
                                  int(height / factor)),
                                 interpolation=cv2.INTER_LINEAR)
        final_height, final_width = final_image.shape[:2]

        colors_width = int(final_width / 6.0)

        image_with_border = cv2.copyMakeBorder(final_image,
                                               top=0,
                                               bottom=0,
                                               left=0,
                                               right=colors_width,
                                               borderType=cv2.BORDER_CONSTANT,
                                               value=[0.0, 0.0, 0.0])

        y_color = 0

        for i, color_LAB in enumerate(colors):
            color_LAB = np.array([[[color_LAB[0], color_LAB[1], color_LAB[2]]]])
            color_LAB = color_LAB.astype(np.uint8)
            color = cv2.cvtColor(color_LAB, cv2.COLOR_Lab2BGR)[0][0]
            color = color.tolist()
            height_color = int(math.ceil(proportions[i]*final_height/float(total_color)))

            cv2.rectangle(image_with_border,
                          (final_width, y_color),
                          (final_width + colors_width, y_color + height_color),
                          color,
                          -1)
            y_color += height_color
        cv2.imshow("colors", image_with_border)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print("Image not found")

if __name__ == "__main__":
    cloth_color(sys.argv[1:][0])

