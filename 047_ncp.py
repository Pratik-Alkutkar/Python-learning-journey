'''
@Author: Pratik Pramod Alkutkar
@Date: 13th Jan 2023 
@Goal: To implemented generalised copy command 
@Commandline: 
    # python ncp.py src_f1 src_f2 src_f3 ..... dest_f 
'''

import sys 

def main(argc:int, argv:list) -> None: 
    '''
    @argc -> argument count 
    @argv -> argument vector 
    main() function of program implementing the logic of ncp
    '''

    # Command line validation 
    if argc < 3: 
        print("UsageError:Correct Usage:%s src_file1 src_file2 ... dest_file" % argv[0])
        sys.exit(-1)

    # Open destination file in write mode 
    try: 
        f_dest_handle = open(argv[argc-1], "w")
    except FileNotFoundError: 
        print("System could not locate the specified file %s" % argv[argv-1])
        sys.exit(-1)
    except PermissionError: 
        print("The application does not have permission to creae file")
        sys.exit(-1)
    except: 
        print("Unexpected error in creating the dest file")
        sys.exit(-1)    

    # Copy every source file in destination file 
    # in the order it appears in command line 
    i=1 
    while i <= argc-2: 
        try: 
            f_src_handle = open(argv[i], "r")
        except FileNotFoundError: 
            print("Invalid source file %s. skipping it" % argv[i])
            i = i + 1 
            continue
        except PermissionError: 
            print("Cannot open %s in read mode. Skipping it" % argv[i])
            i = i + 1
            continue
        except: 
            print("Unexpeted error in opening %s" % argv[i])
            i = i + 1
            continue

        for line in f_src_handle: 
            print(line, file=f_dest_handle, end='')

        f_src_handle.close()

        i = i + 1
       
            
    f_dest_handle.close() 
    
    sys.exit(0) 

main(len(sys.argv), sys.argv)
