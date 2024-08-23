import sys 

def main(argc:int, argv:list)->None: 

    if argc != 2: 
        print("UsageError")
        sys.exit(-1)

    # Step 1: Acquire resource 
    f_handle = open(argv[1], "r")

    # Step 2: Use Resource 
    for line in f_handle: 
        print(line, end='')

    # Step 3: Release Resource 
    f_handle.close()

    sys.exit(0)

main(len(sys.argv), sys.argv)

# OIL -> 
# URANIUM -> 
# Natural gas -> 

# b = tkinter.Button()

# open() -> _io.TextIOWrapper
