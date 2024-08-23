import sys 
import re

def main(): 
    logs = """
    critical message CRITICAL 
    info message INFO 
    mild message MILD
    mild message MILD 
    info message INFO 
    info message INFO 
    mild message MILD 
    critical message CRITCIAL
    info message INFO 
    """

    for line in filter(lambda y : len(y) > 0, map(lambda x : x.strip(), logs.split("\n"))):
        x = re.findall('INFO$', line)
        if x: 
            print(line)
    sys.exit(0)
main() 