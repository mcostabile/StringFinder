import os
import PyPDF2
import re

colors = {
    'red': "\033[91m",
    'green': "\033[92m",
    'yellow': "\033[93m",
    'blue': "\033[94m",
    'default': "\033[0m"
}


def get_files_path(dir, extension):
    files_full_path = [os.path.join(dir, f) for f in os.listdir(
        dir) if f.endswith(extension)]

    return files_full_path


def find_str_in_files(str_to_find, files_dir, extension):
    all_files = get_files_path(files_dir, extension)
    for file in all_files:
        print(f"{colors['blue']}########## {file}{colors['default']}")
        with open(file, 'r') as f:
            if file.endswith(".pdf"):
                fileObj = PyPDF2.PdfFileReader(file)
                totalPages = fileObj.getNumPages()
                for page in range(0, totalPages):
                    pageObj = fileObj.getPage(page)
                    text = pageObj.extractText()
                    line_in_pdf = text.split("\n")
                    for num, line in enumerate(line_in_pdf, -1):
                        line_num = f"{colors['green']}Ln.{num}{colors['default']}"
                        page_num = f"{colors['red']}P. N°{page+1}{colors['default']}"
                        reSearch = re.search(str_to_find, line)
                        if reSearch:
                            matched_line_prettified = line.replace(
                                str_to_find, f"{colors['yellow']}{str_to_find}{colors['default']}"
                            )
                            print(
                                f"{page_num} | {line_num}   {matched_line_prettified}")

            else:
                for num, line in enumerate(f, 1):
                    if str_to_find in line:
                        line_num = f"{colors['green']}Ln.{num}{colors['default']}"
                        matched_line_prettified = line.replace(
                            str_to_find, f"{colors['yellow']}{str_to_find}{colors['default']}"
                        )
                        print(
                            f"{line_num}   {matched_line_prettified.rstrip()}")

        columns, _ = os.get_terminal_size()
        print(f"{colors['blue']}{('-' * columns)}{colors['default']}")
