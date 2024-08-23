def force_comparison(cls:type)->type: 
    required_methods = ['__lt__', '__le__', '__eq__', 
                        '__ne__', '__gt__', '__ge__']
    for method_name in required_methods: 
        if method_name not in cls.__dict__.keys(): 
            raise TypeError("class {} definition does not create comparable objects".format(cls.__name__))
    return cls 

@force_comparison
class CPA_int_1: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __le__(self, other): 
        return self.n <= other.n
    def __lt__(self, other): 
        return self.n < other.n 
    def __ge__(self, other): 
        return self.n >= other.n 
    def __gt__(self, other): 
        return self.n > other.n 
    def __eq__(self, other): 
        return self.n == other.n 
    def __ne__(self, other): 
        return self.n != other.n 
    
@force_comparison
class CPA_int_2: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __le__(self, other): 
        return self.n <= other.n
    def __lt__(self, other): 
        return self.n < other.n 
    def __ge__(self, other): 
        return self.n >= other.n 
  