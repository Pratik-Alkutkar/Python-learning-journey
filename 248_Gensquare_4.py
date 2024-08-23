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
        def get_generator(N:int): 
            for x in range(N): 
                yield x**2 
        G = get_generator(self.N)
        return Gensquare_iterator(G)

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

print("SECOND TIME")
for x in gs: 
    print(x)

print("THIRD TIME")
for x in gs: 
    print(x) 