class C: 
    def __init__(self): 
        self.x = 1.1 
        self.y = 2.2 
        self.z = 3.3 

    def __getattribute__(self, attr_name): 
        if attr_name == 'x': 
            return object.__getattribute__(self, 'x') 
        elif attr_name == 'y': 
            return object.__getattribute__(self, 'y')
        elif attr_name == 'z': 
            return object.__getattribute__(self, 'z')
        else: 
            raise AttributeError("object of 'C' has no attribute {}".format(attr_name))
        
objC = C() 
print(objC.x, objC.y, objC.z)

try: 
    print(objC.m)
except: 
    from sys import exc_info 
    exc_name, exc_data, _ = exc_info() 
    print(exc_name, exc_data)