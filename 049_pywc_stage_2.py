'''
@Author: Pratik Pramod Alkutkar
@Date: 17th Jan 2023 
@Goal: To implement the second stage of pywc command 
@Commandline: # python pywc.py file1 file2 ...
The number of lines, number of charaters and file name
of each line on command line will be printed. 
The last line of ouput will display the total. 
file_1_#LINES   file_1#CHARS    file_1 


file_N_#LINES   file_N_#CHARS   file_n 
total_#LINES    total_#CHARS    total 
The total line should be displayed if number of input files 
is greater than 1 
'''

import sys 

def main(argc:int, argv:list)->None: 

    if argc < 2: 
        print("UsageError:%s file1 file2 ..." % argv[0])
        sys.exit(-1)

    nr_total_lines = 0 
    nr_total_chars = 0 
    
    i = 1 
    
    while i < argc: 
        
        try: 
            f_handle = open(argv[i], "r")
        except FileNotFoundError: 
            print("Invalid path %s" % argv[1])
            sys.exit(-1)
        except PermissionError: 
            print("Permission denied to open %s" % argv[1])
            sys.exit(-1)
        except: 
            print("Unexpected error in opening the file %s" % argv[1])
            sys.exit(-1)
        
        nr_lines = 0 
        nr_chars = 0 
        
        for line in f_handle: 
            nr_lines = nr_lines + 1 
            nr_chars = nr_chars + len(line)
        f_handle.close()
        print(nr_lines, nr_chars, argv[i], sep='\t')    
        nr_total_chars = nr_total_chars + nr_chars 
        nr_total_lines = nr_total_lines + nr_lines 

        i = i + 1 

    if argc > 2: 
        print(nr_total_lines, nr_total_chars, "total", sep='\t')

    sys.exit(0) 

main(len(sys.argv), sys.argv)