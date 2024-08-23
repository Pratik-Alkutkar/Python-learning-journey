import re 
import sys 

def main(): 

    logs = """
    CRITICAL THREAT:some critical message
    INFO:some information warning 
    MILD THREAT:some mild theat 
    INFO:some info 
    CRITICAL:some critcial attack 
    """

    for line in logs.split("\n"): 
        line = line.strip() 
        pattern = '^CRITICAL'
        ret = re.findall(pattern, line)
        if ret: 
            print(line)
    sys.exit(0) 

main()

