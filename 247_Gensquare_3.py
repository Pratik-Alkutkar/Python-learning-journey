class Gensquare_iterator: 
    def __init__(self, G): 
        self.G = G 
    def __next__(self):
        return self.G.__next__()

class Gensquare: 
    def __init__(self, N:int): 
        if type(N) != int: 
            raise TypeError("N must be an integer")
        if N <= 0: 
            raise ValueError("N must be positive")
        self.N = N 

    def __iter__(self): 
        print("In Gensquare.__iter__")
        
        return Gensquare_iterator()
        # How to generate a generator object in __iter__
        # which contains the squares of all elements 
        # from 0 to self.N-1
        # Without this generator object __iter__ will not be 
        # able to create an object of the type Gensquare_iterator

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