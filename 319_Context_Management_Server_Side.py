class Test: 
    def __init__(self, m:int, n:int): 
        print("In Test.__init__")
        assert type(m) == int and type(n) == int, "TypeError for m or n"
        self.m = m 
        self.n = n 

    def __enter__(self): 
        print("In Test.__enter__")
        return self

    def __exit__(self, x, y, z): 
        print("In Test.__exit__")
        return True 

    def use(self):
        from time import sleep  
        print("using the resource",end='', flush=True)
        for i in range(5):
            print(".", end='', flush=True)
            sleep(1)
        print()

def main(): 
    # goal 
    print("about to start with block header")
    with Test(100, 200) as v: 
        v.use() 
    print("just ended executing the with block")

main()
    
"""
COMPLEX RESOURCES 

handle = acquire_resource() # RESOURCE MEMORY CREATE 

some_func_1(handle); 
some_func_2(handle); 
some_func_3(handle); 

RAII 
"""