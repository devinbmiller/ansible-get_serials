# merge-files.py
# This program will take all the text files in a default directory
# read their contents, and write them to a default text file

import os

def get_file_names(folder='configs/'):
    ''' Will list all the files in a directory and return list of file names
        Param1: folder to get file names from
        Returns: list of file names
    '''    
    
    contents = os.listdir(folder)
    return contents

def merge_files(files, folder='configs/', output='merged-files.txt'):
    ''' This will read the contents of each file in the list of file names
        and append their contentsvto a default file name
        Param1: List of file names
        Param2: Folder where the files are located
        Param3: Name of file with merged contents
    '''
    os.chdir(folder)

    for file in files:
        with open(file, 'r') as source_file:
            contents = source_file.read()

            with open(output, 'a') as dest_file:
                dest_file.write(contents)
                dest_file.write('\n')

def main():
    ''' This is the main program function '''
    
    files = get_file_names()
    merge_files(files)

if __name__ == '__main__':
    main()
