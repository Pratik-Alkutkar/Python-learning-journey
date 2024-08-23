import time 

def outer_function(): 
    print("outer_function():entered")
    def inner_function(): 
        print("inner_function():entered")
        time.sleep(2)
        print("inner_function():leaving ")
    print("outer_function() leaving")
    return inner_function 

def main(): 
    print("main():entered")
    X = outer_function() 
    X() 
    Y = outer_function() 
    Y()
    print("id(X):{}, id(Y):{}".format(id(X), id(Y)))
    print("main():leaving")
    
main()