import re 
import sys 

def main(): 
    s = "SVG ceo -> pratik"
    """
    Pattern: star --> + 
    Matches 'ANY' one or more   characters 
    """
    pattern = "c.+e"
    for word in s.split(): 
        L = re.findall(pattern, word)
        print("searching {} in {}".format(pattern, word))
        if len(L) > 0: 
            print(L)
        else: 
            print("pattern not found")    
    sys.exit(0)

main()  