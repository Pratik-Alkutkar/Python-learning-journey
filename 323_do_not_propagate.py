class Test: 
    def __init__(self, m:int, n:int): 
        print("In Test.__init__")
        assert type(m) == int and type(n) == int, "TypeError for m or n"
        self.m = m 
        self.n = n 

    def __enter__(self): 
        print("In Test.__enter__")
        return self

    def __exit__(self, exc_name, exc_data, exc_tb): 
        print("Releasing a resource")
        print("Checking if exception occurred or not")
        if exc_name != None: 
            print("Uncaught exception in with block")
            print("exc_name={}, exc_data={}".format(exc_name, exc_data))
            print("May handle or may not handle")
            print("But will decide whether to propagate it or not")
            print("This implementation of Test chooses NOT to propagate")
            return True
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
        print(X)
    print("just ended executing the with block")

main()

