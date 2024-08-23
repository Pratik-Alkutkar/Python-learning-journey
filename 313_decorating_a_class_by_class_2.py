class force_comparable: 
    def __init__(self, cls:type): 
        if type(cls) != type: 
            raise TypeError 
        self.cls = cls 
        required_method_names = ['__lt__', '__le__', '__eq__', 
                                 '__ne__', '__gt__', '__ge__']
        for method_name in required_method_names: 
            if method_name not in cls.__dict__.keys(): 
                raise TypeError("class {} does not create comparable objects".format(cls.__name__))
        
    def __call__(self, *args, **kwargs): 
        return self.cls(*args, **kwargs)


@force_comparable
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
    
@force_comparable
class CPA_int_2: 
    def __init__(self, init_n): 
        self.n = init_n 

    def __le__(self, other): 
        return self.n <= other.n
    def __lt__(self, other): 
        return self.n < other.n 
    def __ge__(self, other): 
        return self.n >= other.n 
  