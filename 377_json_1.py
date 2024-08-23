import sys 
import json 

def main(): 
    strD = '{"name" : "rohit", "city" : "Pune", "roll" : 30, "marks" : 85.6}' 
    # from dictionary to string conversion 
    D = json.loads(strD)
    for (key, val) in D.items(): 
        print(key, val, type(key), type(val), sep=':')

    sys.exit(0) 

main() 