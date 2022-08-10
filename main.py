from helpers import *
import sys

if __name__ == '__main__':
    try:
        str_to_find = sys.argv[1]
        try:
            files_dir = sys.argv[2]
        except:
            files_dir = "./files_directory"
        try:
            extension = sys.argv[3]
        except:
            extension = ".txt"

        find_str_in_files(str_to_find, files_dir, extension)

    except IndexError:
        print(
            "You must provide at least one argument in the execution!\n"
            "Example: python3 main.py foo"
        )
