import sys 
import os 

def main(argc:int, argv:list)->None: 

    if argc != 2: 
        print("UsageError:{} dir_path".format(argv[0]))
        sys.exit(-1) 

    try: 
        for f_name in os.listdir(argv[1]): 
            print(f_name)
    except: 
        exc_name, exc_data, exc_tb = sys.exc_info()
        print(exc_name, exc_data, sep=':')

main(len(sys.argv), sys.argv) 