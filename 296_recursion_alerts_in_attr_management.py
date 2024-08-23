class Test: 
    def __init__(self, init_n): 
        self.n = init_n 

    def getn(self): 
        return self.__dict__['n'] ** 2 
    
    def setn(self, rhs_object): 
        print("In setn")
        self.n = rhs_object 

    def deln(self): 
        del self.n 
    
    n = property(getn, setn, deln)

t = Test(7)
