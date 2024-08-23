import sys 
import re 

def main(): 
    s1 = "SV"
    s2 = "SVG"
    s3 = "asdfasfasf SV"
    pattern = 'SV\Z'
    ret1 = re.findall(pattern, s1)
    print("ret1:", ret1)
    ret2 = re.findall(pattern, s2)
    print("ret2:", ret2)
    ret3 = re.findall(pattern, s3)
    print("ret3:", ret3)
    sys.exit(0) 

main()