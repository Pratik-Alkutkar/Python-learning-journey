"""
Let B be a class. You want to force class D to derive itself 
from B. If it does not then creation of class D shoud fail. 
Write a code for the same. 

echnique: Decorator 
Check: Fetch base classes list of the Decorated class 
(class_name.__bases__ returns the list immediate base classes)
and check for the membership of class 'B' 
"""

def force_subclassing_of(cls:type): 
    base_cls = cls 
    def real_decorator(cls:type): 
        if base_cls not in cls.__bases__: 
            raise TypeError("{} not deriving from {}".format(cls.__name__, 
                                                             base_cls.__name__))

    return real_decorator 

class B: 
    pass 

@force_subclassing_of(B) 
class D1(B): 
    pass 

@force_subclassing_of(B)
class D2: 
    pass 
#---------------------------------------------------------
def force_subclassing_of(*args): 
    for cls in args: 
        if type(cls) != type: 
            raise TypeError("force_sub_classing_of: only accepts class names")
    saved_required_cls_tuple = args 
    def real_decorator(cls:type): 
        for base_cls in saved_required_cls_tuple: 
            if base_cls not in cls.__bases__: 
                raise TypeError("{} does not derive itself from {}".format(
                    cls.__name__, base_cls.__name__
                ))
    return real_decorator 

# @force_subclassing_of(B1, B2, .., Bn)
#---------------------------------------------------------