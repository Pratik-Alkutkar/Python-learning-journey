class C: 
    def __init__(self): 
        self.x = 1.1 
        self.y = 2.2 
        self.z = 3.3 

    def __getattribute__(self, attr_name): 
        if attr_name in ['x', 'y', 'z']: 
            return self.__dict__[attr_name]
        else: 
            raise AttributeError("{} does not exist in object of class C".format(attr_name))

objC = C() 
print(objC.x)
print(objC.y)
print(objC.z)
print(objC.m)
print(objC.q)

"""
Chain: 
objC.x on RHS (print(objC.x))
--> C.__getattribute__(objC, 'x') # self<-objC, attr_name<-'x' 
--> if attr_name in ['x', 'y', 'z'] got evaluated to True as attr_name == 'x' 
--> return self.__dict__[attr_name]
--> self.__dict__ triggered one more call to __getattribute__
--> self.__dict__ --> C.__getattribute__(objC, '__dict__) 
    self <- objC, attr_name <- '__dict__' 
--> if attr_name in ['x', 'y', 'z'] got evaluated to False because attr_name 
    was neither 'x', 'y', 'z'. 
--> else-> raise AttributeError("{} does not exist in object of class C".format(attr_name))
--> Emitted a message on console 
    '__dict__' does not exist in object of class C
"""