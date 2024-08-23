import re 
import sys 

def main(): 
    L = ['ce', 'coep', 'course', 'core', 'code']
    """
    Pattern -> ? 
    Usage -> .? 
    Match if zero or one occurence of ANY char 
    """
    pattern = 'c.?e'
    for word in L: 
        ret = re.findall(pattern, word)
        if ret: 
            print(word)
    sys.exit(0) 

main() 