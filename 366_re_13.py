import sys 
import re 

def main(): 
    s1 = 'SVG'
    s2 = "Programming must be learnt by going to the Core Level"
    s3 = "This is at the Core"
    s4 = 'CodeCore'
    s5 = "xyzCorepqr"
    s6 = "CodeCore!"
    s7 = "SVG ceo -> pratik"
    s8 = 'SVG Core'
 
    pattern1 = r'\BCore'
    pattern2 = r'Core\B'
    print("searches with pattern 1:{}".format(pattern1))
    ret1 = re.findall(pattern1, s1)
    ret2 = re.findall(pattern1, s2) 
    ret3 = re.findall(pattern1, s3)
    ret4 = re.findall(pattern1, s4)
    print("search 1:{}, serach 2:{}, search 3:{}, serach 4:{}".format(ret1, ret2, ret3, ret4))
    ret5 = re.findall(pattern1, s5)
    ret6 = re.findall(pattern1, s6)
    print("search 5:{}, search 6:{}".format(ret5, ret6))
    ret7 = re.findall(pattern1, s7)
    print("search 7:{}".format(ret7))
    ret8 = re.findall(pattern1, s8)
    print("search 8:{}".format(ret8))

    print("searches with pattern 2{}".format(pattern2))
    ret1 = re.findall(pattern2, s1)
    ret2 = re.findall(pattern2, s2) 
    ret3 = re.findall(pattern2, s3)
    ret4 = re.findall(pattern2, s4)
    print("search 1:{}, serach 2:{}, search 3:{}, serach 4:{}".format(ret1, ret2, ret3, ret4))
    ret5 = re.findall(pattern2, s5)
    ret6 = re.findall(pattern2, s6)
    print("search 5:{}, search 6:{}".format(ret5, ret6))
    ret7 = re.findall(pattern2, s7)
    print("search 7:{}".format(ret7))
    ret8 = re.findall(pattern2, s8)
    print("search 8:{}".format(ret8))
    sys.exit(0) 

main()

'''
    REGULAR ENGINE 
        greedy 
        x
        lazy 
    
'''