import os
import subprocess
import time

number_of_colors_list = [2, 4, 8, 16, 32, 64, 128, 256]

input_folder = "images/input"
# First collect the input files, cause if looping during creation, the output files interfere with the loop.
input_files = [file for file in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, file))]
for input_file in input_files:
    for num_colors in number_of_colors_list:
        base_name = input_file.split(".")[0]
        cmd_str = f"/Applications/GIMP.app/Contents/MacOS/gimp -i -b " \
                  f"'(batch-convert-rgb-indexed \"images/input/{input_file}\" {num_colors})' -b '(gimp-quit 0)'; " \
                  f"mv images/input/{base_name}-{num_colors}.png images/output"
        print(cmd_str)
        subprocess.run(cmd_str, shell=True)

