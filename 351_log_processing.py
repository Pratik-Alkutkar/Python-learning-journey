import sys 
import re 

def main(): 

    log = """
    [2023:07:09:07:38]  some message
    [2023:07:09:10:56]  some message
    [2023:07:09:15:21]  some message
    [2023:07:10:06:05]  some message
    [2023:07:10:13:45]  some message
    [2023:07:10:23:57]  some message
    [2023:07:10:12:43]  some message
    [2023:07:11:03:16]  some message
    [2023:07:11:06:52]  some message
    """

    """for line in log.split('\n'):
        line = line.strip()
        if len(line) > 0: 
            #print(line)
            L = line.split(' ')
            #print(L)
            #print(L[0])
            #print(L[0][1:len(L[0])-1])
            X = L[0][1:len(L[0])-1].split(":")
            #print(X)
            #print(X[2])
            X = re.findall('1\d', X[2])
            if len(X) > 0: 
                print(line)
    """
    #-------------------------------------------------------
    for line in log.split('\n'): 
        if len(line.strip()) > 0:
            date = line.strip().split(' ')[0][1:-1].split(':')[2]
            print(date)
    
    L = [line.strip().split(' ')[0][1:-1].split(':')[2] for line in log.split('\n') if len(line.strip()) > 0]
    print(L)
    sys.exit(0)
main()
        



