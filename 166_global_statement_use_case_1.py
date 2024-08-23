num = 100 

def test(): 
    global num 
    num = 500 

def main(): 
    print("BEFORE test():Global num:", num)
    test() 
    print("AFTER test():Global num:", num)

main()