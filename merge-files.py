# merge-files.py
# This program will take all the text files in a default directory
# read their contents, and write them to a default text file

import os, sys


def get_file(folder):
    """ This is a generator function that will return one file name 
        from a folder at a time.
        Param1: string of folder to get files from
    """
    for file in os.listdir(folder):
        yield file


def merge_files(folder="configs/", output="configs/merged-files.txt"):
    """ This will read the contents of each file in the list of file names
        and append their contents to a default file name
        Param1: Folder where the files are located
        Param2: Name of file with merged contents
    """
    for file in get_file(folder):
        with open(os.path.join(folder, file), "r") as source_file:
            contents = source_file.read()

            with open(output, "a") as dest_file:
                dest_file.write(contents)
                dest_file.write("\n")

    print("\n\nAll files merged to: " + output + "\n\n")


def main(cmd_ln_args):
    """ This is the main program function
        Param1: sys.argv list
    """
    output_file = cmd_ln_args[1] + "-merged.txt"
    merge_files(cmd_ln_args[1], output_file)


if __name__ == "__main__":
    main(sys.argv)
