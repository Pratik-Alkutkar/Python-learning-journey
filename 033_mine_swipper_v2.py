import sys 

def easy_level(): 
    print("@easy level function")

def intermediate_level(): 
    print("@intermediate level function")

def expert_level(): 
    print("@expert level function")

def help(): 
    print("To select level: mineswipper.py -easy or -intermediate or -expert")
    print("To get help: mineswipper.py -help")

def main(argc:int, argv:list): 

    if argc == 1: 
        help()
        sys.exit(0) 

    if argc > 2:
        print("Invalid command line") 
        help()
        sys.exit(-1)

    if argv[1] == '-easy': 
        easy_level() 
    elif argv[1] == '-intermediate': 
        intermediate_level() 
    elif argv[1] == '-expert': 
        expert_level() 
    elif argv[1] == '-help': 
        help() 
    else: 
        print("Invalid command line argument")
        help() 
        sys.exit(-1)

    sys.exit(0) 

main(len(sys.argv), sys.argv) 