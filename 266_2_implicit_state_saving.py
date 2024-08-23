import time 

def outer_function(N): 
    print("outer_function():entered")
    def inner_function(): 
        m = N 
        print("inner_function():entered")
        time.sleep(2)
        print("m:", m)
        print("inner_function():leaving ")
    print("outer_function() leaving")
    return inner_function 

def main(): 
    print("main():entered")
    X = outer_function(100) 
    Y = outer_function(200) 
    X() # m: 100 
    Y() # m: 200
    print("id(X):{}, id(Y):{}".format(id(X), id(Y)))
    print("main():leaving")
    
main()