import sys 

class Date: 
    def __init__(self): 
        self.day = 1 
        self.month = 1 
        self.year = 1970 

def main(): 
    D = Date()
    print("type(D):", type(D))
    print("D.__dict__:", D.__dict__)
    sys.exit(0) 

main()