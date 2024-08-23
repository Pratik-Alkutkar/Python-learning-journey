import sys 

def main(argc:int, argv:list)->None: 
    if argc != 2: 
        print("UsageError")
        sys.exit(-1)
    
    with open(argv[1], "r") as f_handle: 
        for line in f_handle: 
            print(line, end='')
       
    sys.exit(0)

main(len(sys.argv), sys.argv)