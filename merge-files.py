# merge-files.py
# This program will take all the text files in a default directory
# read their contents, and write them to a default text file

import os, sys


def usage():
    """ Gives the user a usage message if they do noy type enough
        command line arguments
    """
    print(
        """
    USAGE:
    python merge-files.py <directory>

    directory: location of files you would like to merge
    """
    )


def get_file(folder):
    """ This is a generator function that will return one file name 
        from a folder at a time.
        Param1: string of folder to get files from
        Yields: String file name
    """
    files = [
        file
        for file in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, file))
    ]

    if files:
        for file in files:
            yield file
    else:
        print("No file(s) found in: " + folder)
        sys.exit(0)


def open_file(folder):
    """ This is a generator function that will yield an open file object.
        It uses the get_file generator function to get the file name to open.
        Param1: String of folder to get files from
        Yields: Open file object
    """
    for file in get_file(folder):
        yield open(os.path.join(folder, file), "r")


def merge_files(folder="configs/", output="configs/merged-files.txt"):
    """ This will read the contents of each file in the list of file names
        and append their contents to a default file name
        Param1: Folder where the files are located
        Param2: Name of file with merged contents
    """
    for file in open_file(folder):
        contents = file.read()

        with open(output, "a") as dest_file:
            dest_file.write(contents)
            dest_file.write("\n")

    print("\n\nAll files merged to: " + output + "\n\n")


def main(cmd_ln_args):
    """ This is the main program function
        Param1: sys.argv list
    """
    if len(cmd_ln_args) <= 1:
        usage()
    else:
        src_folder = cmd_ln_args[1]  # where to look for the files, arg from cmd line
        output_file = src_folder + "-merged.txt"  # what output file will be named

        merge_files(src_folder, output_file)


if __name__ == "__main__":
    main(sys.argv)
