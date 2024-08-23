"""
@Goal: This file specifies pattern iterator 
How to make object of type T compatible with for loop 
"""

class T_iterator: 
    # G is an object of type generator 
    def __init__(self, G): 
        self.G = G 
    def __next__(self): 
        return self.G.__next__()
    
class T: 
    def __init__(self, zero_or_more_init_params): 
        pass 
        # Replace pass with constructor definition which 
        # creates attributes in self and assigns those attributes 
        # to values. 

    def __iter__(self): 
        def get_generator(appropriate_formal_parameters): 
            pass 
            # Replace pass by a computational logic which will 
            # yield all objects that you want in generator 
        return T_iterator(get_generator(appropriate_actual_params))
    
objT = T(initialization_data)
for t in objT: 
    pass 
    # replace pass with 'do something with t' 