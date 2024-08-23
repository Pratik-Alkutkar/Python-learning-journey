import re 
import sys 

def main(): 
    L = ['ce', 'coep', 'course', 'core', 'code']
    """
    Pattern -> {n} 
    Usage -> .{n}
    Match if n number of ANY chars  
    """
    pattern = 'c.{2}e'
    for word in L: 
        ret = re.findall(pattern, word)
        if ret: 
            print(word)
    sys.exit(0) 

main() 