class C: 
    def __init__(self): 
        self.x = 1.1 
        self.y = 2.2 
        self.z = 3.3 
 
objC = C() 

print("first")
print(objC.x) 
print(objC.y)
print(objC.z)

print("second")
print(objC.__dict__['x'])
print(objC.__dict__['y'])
print(objC.__dict__['z'])

print("third")
print(objC.__getattribute__('x'))
print(objC.__getattribute__('y'))
print(objC.__getattribute__('z'))

print("C.__mro__:", C.__mro__)

if '__getattribute__' in dir(object): 
    print("__getattribute__ is present in class object")

print("fourth")
print(object.__getattribute__(objC, 'x'))
print(object.__getattribute__(objC, 'y'))
print(object.__getattribute__(objC, 'z'))
