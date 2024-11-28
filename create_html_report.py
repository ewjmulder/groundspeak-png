import os


number_of_colors_list = [2, 4, 8, 16, 32, 64, 128, 256]


def main():
    css = "img { float: left; } " \
          "@media print { .pagebreak { page-break-before: always; }}"
    html = f"<!DOCTYPE html><html><head><style>{css}</style></head><body>"
    input_folder = "images/input"
    output_folder = "images/output"
    input_files = sorted(file for file in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, file)))
    output_files = sorted(file for file in os.listdir(output_folder) if os.path.isfile(os.path.join(output_folder, file)))
    for input_file in input_files:
        html += "<table border='1' cellspacing='0' width='900px'>"
        original_size = get_file_size(f"images/input/{input_file}")
        base_name = input_file.split(".")[0]
        [index, name_with_underscores, zoom_level, x, y] = base_name.split("-")
        name = name_with_underscores.replace("_", " ")
        html += f"<tr><td rowspan='5' width='512px'><img src='../input/{input_file}'></td>" \
                f"<th colspan='2'>Name</th><td colspan='2'>{name}</td></tr>"
        html += f"<tr><th colspan='2'>Zoom level</th><td colspan='2'>{zoom_level}</td></tr>"
        html += f"<tr><th colspan='2'>X</th><td colspan='2'>{x}</td></tr>"
        html += f"<tr><th colspan='2'>Y</th><td colspan='2'>{y}</td></tr>"
        html += f"<tr><th colspan='2'>Size</th><td colspan='2'>{original_size}</td></tr>"

        comparison_file = list(filter(lambda file: file.startswith(f"{base_name}-comparison"), output_files))[0]
        html += f"<tr><td colspan='5'>&nbsp;</td></tr>" \
                f"<tr><td></td>" \
                f"<th>#colors</th><th>size</th><th>% of original</th><th>comparison score</th></tr>"
        for index, num_colors in enumerate(number_of_colors_list):
            html += "<tr>"
            if index == 0:
                html += f"<td rowspan='8'><img src='../output/{comparison_file}'></td>"
            converted_file = f"images/output/{base_name}-{num_colors}.png"
            converted_size = get_file_size(converted_file)
            percentage_size = "{:.2f}%".format((converted_size / original_size) * 100)
            comparison_data = comparison_file.replace(".png", "").split("-")
            comparison_score = comparison_data[6:14][index]

            html += f"<td>{num_colors}</td><td>{converted_size}</td>" \
                    f"<td>{percentage_size}</td><td>{comparison_score}</td></tr>"
            html += "</tr>"
        html += "</table><br /> <br />"
        html += "<div class='pagebreak'></div>"
    html += "</html>"
    with open("images/output/report.html", "w") as text_file:
        text_file.write(html)


def get_file_size(filename):
    file_stats = os.stat(filename)
    return file_stats.st_size


main()
