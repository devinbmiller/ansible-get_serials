# merge-files.py
# This program will take all the text files in a default directory
# read their contents, and write them to a default text file

import os


def merge_files(folder="configs/J-West", output="configs/merged-files.txt"):
    """ This will read the contents of each file in the list of file names
        and append their contents to a default file name
        Param1: List of file names
        Param2: Folder where the files are located
        Param3: Name of file with merged contents
    """
    files = os.listdir(folder)

    for file in files:
        with open(os.path.join(folder, file), "r") as source_file:
            contents = source_file.read()

            with open(output, "a") as dest_file:
                dest_file.write(contents)
                dest_file.write("\n")

    print("\n\nAll files merged to: " + os.path.join(folder, output) + "\n\n")


def main():
    """ This is the main program function """

    merge_files()


if __name__ == "__main__":
    main()
