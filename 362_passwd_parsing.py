import sys 
import re

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

    lines = f_handle.readlines() 
    print("type(lines):", type(lines))
    lines = list(filter(lambda line : len(line) > 0, lines))
    for i in range(len(lines)): 
        lines[i] = lines[i].strip() 

    for line in lines: 
        ret = re.findall('nologin\Z | false\Z', line)
        if ret: 
            print(line.split(":")[0])

    f_handle.close() 
    sys.exit(0)

main(len(sys.argv), sys.argv)