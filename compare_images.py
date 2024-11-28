import cv2
import os
import numpy as np

DIFF_EXPONENT = 2
number_of_colors_list = [2, 4, 8, 16, 32, 64, 128, 256]


def compare(img1, img2):
    (height, width, colors) = img1.shape
    sum_diffs = 0
    for y in range(0, height):
        for x in range(0, width):
            sum_diff_pixel = 0
            for color_index in range(0, colors):
                color1 = int(img1[y][x][color_index])
                color2 = int(img2[y][x][color_index])
                diff = abs(color1 - color2)
                sum_diff_pixel += diff
            sum_diffs += (sum_diff_pixel / 3) ** DIFF_EXPONENT

    return sum_diffs / (height * width)


input_folder = "images/input"
# First collect the input files, cause if looping during creation, the output files interfere with the loop.
input_files = [file for file in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, file))]
for input_file in input_files:
    base_name = input_file.split(".")[0]
    img1 = cv2.imread(f"images/input/{input_file}")
    (height, width, colors) = img1.shape
    comparison_img = []
    diff_string = ""
    for i in range(0, len(number_of_colors_list)):
        # TODO: iter with index
        num_colors = number_of_colors_list[i]
        img2 = cv2.imread(f"images/output/{base_name}-{num_colors}.png")
        start_row = int((i / len(number_of_colors_list)) * height)
        end_row = start_row + int(height / len(number_of_colors_list))
        for row in range(start_row, end_row):
            half = int(width / 2)
            comparison_img.append(img1[row][0:half].tolist() + [[0, 0, 0]] + img2[row][half:].tolist())
        comparison_img.append([[0, 0, 0] for i in range(0, width + 1)])
        diff = compare(img1, img2)
        print(f"Diff between {base_name} for {num_colors} colors:\t {diff}")
        diff_string += "-{:.2f}".format(diff)
    cv2.imwrite(f"images/output/{base_name}-comparison{diff_string}.png", np.array(comparison_img))
