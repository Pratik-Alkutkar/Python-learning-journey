'''
@Author: Pratik Pramod Alkutkar
@Date: 11th Jan 2023 
@Goal: To implement the copy command. 
@Commandline: 
# python cpa_copy.py src_file dest_file 
src_file -> Must exist 
dest_file -> May or may not exist. 
if destination file does not exist it will 
be created but if it exists and already contains 
some data then the existing data will be truncated 
and copying process will happen. 
'''

import sys 

def main(argc:int, argv:list)->None: 

    if argc != 3:
        print("UsageError:Correct Usage:%s src_file dest_file" % argv[0])
        sys.exit(-1)

    f_src_handle = open(argv[1], "r")
    f_dest_handle = open(argv[2], "w")

    for line in f_src_handle: 
        print(line, file=f_dest_handle, end='')
    
    f_src_handle.close() 
    f_dest_handle.close()

    sys.exit(0) 

main(len(sys.argv), sys.argv)