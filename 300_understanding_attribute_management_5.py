import sys 

class C: 
    def __init__(self): 
        self.x = 1.1 
        self.y = 2.2 
        self.z = 3.3 

    def __getattribute__(self, attr_name): 
        if attr_name == '__dict__': 
            return object.__getattribute__(self, '__dict__')
        else: 
            return self.__dict__[attr_name]
        
objC = C()
print(objC.x)


# objC.x -> C.__getattribute__(objC, 'x') 
# else -> self.__dict__[attr_name]
# for self.__dict__ -> C.__getattribute__(self, '__dict__') -> {'x':1.1, 'y':2.2, 'z':3.3
# return {'x':1.1, 'y':2.2, 'z':3.3}['x']