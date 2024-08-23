class X: 
    def __add__(self, other): 
        print("In X.__add__")
        print("id(self):{} id(other):{}".format(id(self), id(other)))
        return None 
    
x1 = X() 
x2 = X() 
print("id(x1):{}, id(x2):{}".format(id(x1), id(x2)))

rs = x1 + x2 # x1.__add__(x2) -> X.__add__(x1, x2)
#print("rs:", rs)

