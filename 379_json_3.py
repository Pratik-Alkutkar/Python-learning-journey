import sys 
import json 

def main(): 
    b1 = True 
    b2 = False 
    n = 156984 
    f = 3.141568 
    s1 = "Hello JSON!"
    T = (True, 10, 3.14)
    L = [100, 200, 300, 400]
    D = {"a":1000, "b":2000, True:3000, False:4000}
    S = None

    s = json.dumps(b1)
    print("b1:s:{}, type(s):{}".format(s, type(s)))
    s = json.dumps(b2)
    print("b2:s:{}, type(s):{}".format(s, type(s)))
    s = json.dumps(n)
    print("n:s:{}, type(s):{}".format(s, type(s)))
    s = json.dumps(f)
    print("f:s:{}, type(s):{}".format(s, type(s)))
    s = json.dumps(s1)
    print("s1:s:{}, type(s):{}".format(s, type(s)))
    s = json.dumps(T)
    print("T:s:{}, type(s):{}".format(s, type(s)))
    s = json.dumps(L)
    print("L:s:{}, type(s):{}".format(s, type(s)))
    s = json.dumps(D)
    print("D:s:{}, type(s):{}".format(s, type(s)))
    s = json.dumps(S)
    print("S:s:{}, type(s):{}".format(s, type(s)))

    sys.exit(0) 
main()