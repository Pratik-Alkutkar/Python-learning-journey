class dec: 
    def __init__(self, cls:type): 
        if type(cls) != type: 
            raise TypeError("cls must be a class")
        self.cls = cls 
        print("Name of class:{}".format(cls.__name__))

    def __call__(self, *args, **kwargs): 
        return self.cls(*args, **kwargs)

@dec
class Test: 
    def __init__(self, init_x, init_y): 
        self.x = init_x 
        self.y = init_y 

    def getx(self): return self.x 
    def gety(self): return self.y 
    def setx(self, x): self.x = x 
    def sety(self, y): self.y = y 


objTest = Test(100, 200)
print(objTest.getx(), objTest.gety())
