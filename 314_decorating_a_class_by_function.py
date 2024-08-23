def dec(cls): 
    print("The name of decorated class:{}".format(cls.__name__))
    return cls 

@dec 
class Test: 
    a = 10 
    b = 20 
    def __init__(self, init_x, init_y): 
        self.x = init_x 
        self.y = init_y 

    def compute(self): 
        return self.x + self.y
    
# cls namespace : {'a':10, 'b':20, '__init__' : func object, 'compute': func object}


