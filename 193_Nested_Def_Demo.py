import time 

def outer_function():
    print("Entered outer function")
    def inner_function():
        print("Entered inner function")
        time.sleep(2)
        print("Leaving inner function")
    inner_function()
    print("Leaving outer function")
    
outer_function()
        
