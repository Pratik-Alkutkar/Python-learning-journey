"""
How will force a particular class to keep its object 
compatible with for loop? Write a structure of a code 
or complete code. 

Technique: Decorator. 
Check: decorated class class must contain __iter__ 
"""

def force_iterable(cls:type)->type: 
    if '__iter__' not in cls.__dict__.keys(): 
        raise TypeError("Object of {} is not iterable".format(cls.__name__))
    return cls

class Array1_iterator:
    def __init__(self, G): 
        self.G = G 
    def __next__(self): 
        return self.G.__next__()

@force_iterable
class Array1: 
    def __init__(self, size:int): 
        if type(size) != int: 
            raise TypeError 
        if size < 0: 
            raise ValueError 
        self.L = [0 for i in range(size)]

    def __iter__(self): 
        def get_generator(lst:list): 
            for x in lst: 
                yield x 
        return Array1_iterator(get_generator(self.L))

@force_iterable
class Array2: 
    def __init__(self, size:int): 
        if type(size) != int: 
            raise TypeError 
        if size < 0: 
            raise ValueError 
        self.L = [0 for i in range(size)]


