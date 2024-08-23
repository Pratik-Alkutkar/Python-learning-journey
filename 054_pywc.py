'''
@Author: Pratik Pramod Alkutkar 
@Date: 17th Jan 2023 
@Goal: To implement the pywc command 
@Commandline: # python pywc.py file1 file2 ...
The number of lines, number of words and number 
of charaters and file name of each line on command 
line will be printed. The last line of ouput will 
display the total. 

file_1_#LINES   file_1#WORDS    file_1#CHARS    file_1 


file_N_#LINES   file_N_#WORDS   file_N_#CHARS   file_n 
total_#LINES    total_#WORDS    total_#CHARS    total 

The total line should be displayed if number of input files 
is greater than 1 
'''

import sys 

def word_count(s:str)->int: 
    '''
    @input: s: string for word counting 
    @output: Number of words 
    A space, a tab or a newline is considered to be 
    separator of group of characters defined as words. 
    This algorithm counts word as per above notion of 'word'
    '''

    if type(s) != str: 
        raise TypeError("Word count requires string input")

    IN = 0 
    OUT = 1 
    state = OUT 
    w_cnt = 0 

    for c in s: 
        if state == OUT and not (c == ' ' or c == '\t' or c == '\n'): 
            state = IN 
            w_cnt = w_cnt + 1 
        elif state == IN and (c == ' ' or c == '\t' or c == '\n'): 
            state = OUT 

    return w_cnt 

def main(argc:int, argv:list)->None: 

    if argc < 2: 
        print("UsageError:%s file1 file2 ..." % argv[0])
        sys.exit(-1)

    nr_total_lines = 0 
    nr_total_chars = 0 
    nr_total_words = 0 

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
        nr_words = 0 

        for line in f_handle: 
            nr_lines = nr_lines + 1 
            nr_chars = nr_chars + len(line)
            nr_words = nr_words + word_count(line)
        f_handle.close()
        print(nr_lines, nr_words, nr_chars, argv[i], sep='\t')    
        
        nr_total_chars = nr_total_chars + nr_chars 
        nr_total_lines = nr_total_lines + nr_lines 
        nr_total_words = nr_total_words + nr_words 
        
        i = i + 1 

    if argc > 2: 
        print(nr_total_lines, nr_total_words, nr_total_chars, "total", sep='\t')

    sys.exit(0) 

main(len(sys.argv), sys.argv)

    