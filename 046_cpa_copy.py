'''
@Author: Pratik Pramod Alkutkar
@Date: 13th Jan 2023 
@Goal: To implement copy comment with exception handling 
@Commandline: # python cpa_copy.py src_file dest_file 
src_file must exist 
destination file may or may not exist. 
If destination does not exist -> will be created
If destination does exist -> then exiting data will be truncated 
''' 

import sys 

def main(argc:int, argv:list)->None:
    '''
    @argc: Argument count 
    @argv: Argument vector 
    main() function of program implements the logic of copy command 
    ''' 

    if argc != 3: 
        print("UsageError:Correct Usage:%s src_file dest_file" % argv[0])
        sys.exit(-1)

    try: 
        f_src = open(argv[1], "r")
    except FileNotFoundError: 
        print("System could not find the specified file %s" % argv[1])
        sys.exit(-1)
    except PermissionError: 
        print("The application does not have adequate permission to read file")
        sys.exit(-1)
    except: 
        print("Unexpected error in opening source file")
        sys.exit(-1)

    try: 
        f_dest = open(argv[2], "w")
    except FileNotFoundError: 
        print("System could not file specified file")
        sys.exit(-1)
    except PermissionError: 
        print("The application does not have adequate permission to write on file")
        sys.exit(-1)
    except: 
        print("Unexpected error in opening source file")
        sys.exit(-1)

    for line in f_src: 
        print(line, file=f_dest, end='')
    
    f_src.close()
    f_dest.close()

main(len(sys.argv), sys.argv)
