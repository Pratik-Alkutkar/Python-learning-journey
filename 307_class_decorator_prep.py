"""
    Write a function which acccepts class name as input 
    and determines whether objects of that class are comparable 
    for all comparison operators 
"""

def are_class_object_comparable(cls:type)->bool: 
    required_methods = ['__lt__', '__le__', '__eq__', 
                        '__ne__', '__gt__', '__ge__']
    for method_name in required_methods: 
        if method_name not in dir(cls): 
            return False 
    return True 
