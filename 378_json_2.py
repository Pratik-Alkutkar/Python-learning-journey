import sys 
import json 

def main(): 
    D = {"name" : "rohit", "city" : "Pune", "roll" : 30, "marks" : 85.6}
    strD = json.dumps(D)
    print(strD, type(strD))

    sys.exit(0) 

main()

