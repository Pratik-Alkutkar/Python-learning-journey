import sys 
import re 

def main(): 

    s = 'SVG ceo -> pratik'
    pattern = '\ACore'
    ret = re.findall(pattern, s)
    print(ret)
    if ret != None: 
        print("Match is found")
    else: 
        print("Match is not found")

main()