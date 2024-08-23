"""
@Goal: To write a program which accepts directory path on command line 
        The program must recursively traverse through the directory, printing 
        all the file and folder names along the process. 
@Command line: 

# python recursive_directory_traversal.py dir_path 
"""

import sys 
import os 

def main(argc: int, argv: list) -> None: 

    if argc != 2: 
        print("UsageError:{} dir_path".format(argv[0]))
        sys.exit(-1)
    
    for (dir_name, subdir_lst, nondir_lst) in os.walk(argv[1]): 
        print(dir_name)
        print("\tSubdirectories in {}".format(dir_name))
        for d_name in subdir_lst: 
            print("\t\t{}".format(d_name))
        print("\tNondirectory files in {}".format(dir_name))
        for f_name in nondir_lst: 
            print("\t\t{}".format(f_name))
    
    sys.exit(0)

main(len(sys.argv), sys.argv)