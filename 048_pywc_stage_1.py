'''
@Author: Pratik Pramod Alkutkar
@Date: 17th Jan 2023 
@Goal: To implement the first stage of pywc command 
@Commandline: # python pywc.py file_path 
The number of lines and number of charaters in file_path 
will be displayed. 
'''

import sys 

def main(argc:int, argv:list)->None: 

    if argc != 2: 
        print("UsageError:%s file_path" % argv[0])
        sys.exit(-1)

    try: 
        f_handle = open(argv[1], "r")
    except FileNotFoundError: 
        print("Invalid path %s" % argv[1])
        sys.exit(-1)
    except PermissionError: 
        print("Permission denied to open %s" % argv[1])
        sys.exit(-1)
    except: 
        print("Unexpected error in opening the file %s" % argv[1])
        sys.exit(-1)

    nr_chars = 0 
    nr_lines = 0 
    for line in f_handle: 
        nr_lines = nr_lines + 1 
        nr_chars = nr_chars + len(line)
    f_handle.close()
    print(nr_lines, nr_chars, argv[1], sep='\t')

    sys.exit(0)

main(len(sys.argv), sys.argv)
