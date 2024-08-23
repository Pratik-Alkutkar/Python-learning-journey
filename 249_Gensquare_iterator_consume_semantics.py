class Gensquare: 
    def __init__(self, N:int): 
        if type(N) != int: 
            raise TypeError 
        if N <= 0: 
            raise ValueError 
        self.N = N 
        def get_generator(N:int): 
            for x in range(N): 
                yield x**2 
        self.G = get_generator(self.N)

    def __iter__(self): 
        return self 
    
    def __next__(self): 
        return self.G.__next__()



def main(): 
    gs = Gensquare(5)
    print("FIRST TIME ITERATION")
    for x in gs: 
        print(x) 
    # 0, 1, 4, 16 
    print("SECOND TIME ITERATION")
    for x in gs: 
        print(x)
    # BLANK 

main()