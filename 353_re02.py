import sys 
import re 

def main(): 
    s = "Price of mobile can go upto $2000, I got mine for $589"
    # \d is a special character sequence. 
    # there are several such special character sequences which are supported by re 
    pattern = '\d'
    L = re.findall(pattern, s)
    for digit in L: 
        print(digit)
    sys.exit(0) 

main() 