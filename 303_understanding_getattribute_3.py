class C: 
    def __init__(self): 
        self.x = 1.1 
        self.y = 2.2 
        self.z = 3.3 

objC = C() 
cx = object.__getattribute__(objC, 'x')
cy = object.__getattribute__(objC, 'y')
cz = object.__getattribute__(objC, 'z')
dict_of_objC = object.__getattribute__(objC, '__dict__')

print("cx:{}, cy:{}, cz:{}, dict_of_objC:{}".format(cx, cy, cz, dict_of_objC))

print(objC.x) # C.__getattribute__(objC, 'x')
              # object.__getattribute__(objC, 'x')

""" 
struct C{
    double x, y, z; 
}; 

struct C objC; 

objC.z;     // addr(objC) + 16 -> access  
"""