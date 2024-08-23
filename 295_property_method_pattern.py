"""
class -> Test 
attribute name -> attr 
object name t. 
"""

class Test: 
    def __init__(self, init_data): 
        self.attr = init_data 

    def get_method_of_attr(self): 
        # Logic 

    def set_method_of_attr(self, rhs_object): 
        # Logic 

    def del_method_of_attr(self): 
        # Logic 

    attr = property(get_method_of_attr, 
                    set_method_of_attr, 
                    del_method_of_attr)
    
# client 

t = Test(init_data) 

lhs = t.n # Test.get_method_of_attr(t) 

t.n = rhs # Test.set_method_of_attr(t, rhs)

del t.n # Test.del_method_of_attr(t)

"""
If you want to access 'attr' in get_method_of_attr then 
DON'T use expression 
self.attr 
Use 
self.__dict__['attr']

Simiarly, if you want to use 'attr' on LHS in set_method_of_attr 
then DON't USE expression 
self.attr = rhs 
instead use 
t.__dict__['attr'] = rhs 

If you want to delete attr in del_method_of_attr then do not 
use expression del self.attr 
instead use 

del self.__dict__['attr']
"""

