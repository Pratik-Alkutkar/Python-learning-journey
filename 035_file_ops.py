'''
@Author: Pratik Pramod Alkutkar
@Date: 6th Jan 23 
@Goal: To demonstrate following operations on text file 
        a)  Create 
        b)  Write 
        c)  Read 
        d)  Open 
        e)  Close 
        using Python built in functions (aka high level file handling)

        File name will be accepted from commandline. 

        # file_ops.py file_name
'''

import sys 

def main(argc:int, argv:list)->None: 
    '''
    @input: 
    @argc: Argument count 
    @argv: Argument vector 

    Accepts a file name on command line and 
    performs basic create, open, close, read, 
    write operations on the file 
    '''
    
    if argc != 2: 
        print("UsageError:Correct Usage Is:%s file_name" % argv[0])
        sys.exit(-1)

    f_handle = open(argv[1], "w")
    print("Pratik Alkutkar", file=f_handle)
    print("Python Programmer", file=f_handle)
    print("SVG", file=f_handle)
    print("Contact: - ", file=f_handle)
    print("email: @gmail.com", file=f_handle)
    f_handle.close() 
    
    sys.exit(0) 

main(len(sys.argv), sys.argv)

"""
w -> write 
    NOT PRESENT 
        CREATE BASENAME IN DIRNAME 
        (PROVIDED DIRNAME EXISTS & VALID)
    PRESENT 
        TRUNCATE (=REMOVE) THE EXISTING DATA 
        FROM FILE

r -> read 
    NOT PRESENT 
        raise FileNotFoundError 
    PRESENT 
        LOAD MEDATA WITHOUT REMOVING DATA 
        SET READ WRITE POSITION AT THE START 

a -> append
    NOT PRESENT 
        CREATE BASENAME IN DIRNAME 
        (PROVIDED DIRNAME EXISTS & VALID)
    PRESENT 
        LOADS METADATA WITHOUT REMOVING THE DATA 
        SETS READ WRITE POSITION(=OFFSET) AT THE END 

BASE NAME IS PRESENT IN DIR NAME 
BASE NAME IS NOT PRESENT IN DIR NAME 

'abc.txt' 

CURRENT_WORKING_DIRECTORY\abc.txt
DIRNAME                    BASENAME 
"""