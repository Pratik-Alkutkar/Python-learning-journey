class Gensquare: 
    def __init__(self, N:int): 
        if type(N) != int: 
            raise TypeError("N must be an integer")
        if N <= 0: 
            raise ValueError("N must be positive")
        self.N = N 

    def __iter__(self): 
        print("In Gensquare.__iter__")
        # return None 


try: 
    gs = Gensquare(0)
except ValueError as e:
    print(e) 

try: 
    gs = Gensquare(-5)
except ValueError as e: 
    print(e) 

gs = Gensquare(5)

try: 
    for x in gs: 
        print(x) 
except TypeError as e: 
    print(e)  