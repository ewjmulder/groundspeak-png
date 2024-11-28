import numpy as np
import cv2
import sys
import math

# to_compare = ["4black", "4white"]
# img1 = cv2.imread(f"images/experiment/{to_compare[0]}.png")
# img2 = cv2.imread(f"images/experiment/{to_compare[1]}.png")
to_compare = ["test", "test-256"]
img1 = cv2.imread(f"images/input/{to_compare[0]}.png")
img2 = cv2.imread(f"images/output/{to_compare[1]}.png")
# print(img1)
# print(img2)
(height, width, colors) = img1.shape
diff_punishment = 2
sum_diffs = 0
for y in range(0, height):
    for x in range(0, width):
        sum_diff_pixel = 0
        for color_index in range(0, colors):
            color1 = int(img1[y][x][color_index])
            color2 = int(img2[y][x][color_index])
            diff = abs(color1 - color2)
            sum_diff_pixel += diff
#            print(color1, color2, diff, sum_diff_pixel)
        sum_diffs += (sum_diff_pixel / 3) ** diff_punishment
 #       print((sum_diff_pixel / 3) ** 2)

max_diff_per_pixel = 255 ** diff_punishment
mse = sum_diffs / (height * width)
print(mse)
# me_pct = mse / max_diff_per_pixel
# print(sum_diffs, mse, me_pct)
# print("Difference:", round(me_pct * 100, 2), "%")


