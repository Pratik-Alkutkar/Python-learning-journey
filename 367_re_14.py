import sys 
import re

def main(): 
    s1 = "SVG12"
    s2 = "SVG"
    s3 = "1234"
    pattern = '\D'
    ret1 = re.findall(pattern, s1)
    ret2 = re.findall(pattern, s2)
    ret3 = re.findall(pattern, s3)
    print("search 1:{}, search 2:{}, search 3:{}".format(ret1, ret2, ret3))

    sys.exit(0)

main()