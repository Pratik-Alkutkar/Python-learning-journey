import sys 

def main(argc:int, argv:list)->None: 

    if argc != 2: 
        print("UsageError:Correct Usage:%s file_path" % argv[0])
        sys.exit(-1)

    try: 
        f_handle = open(argv[1], "r")
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data, sep=':')
        sys.exit(-1)

    X = f_handle.readlines() 
    print("type(X):", type(X))
    X = list(filter(lambda line : len(line) > 0, X))
    for i in range(len(X)): 
        X[i] = X[i].strip() 
    print(X)
    f_handle.close() 
    sys.exit(0)

main(len(sys.argv), sys.argv)