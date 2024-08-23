class Date: 
    pass 

d = Date() 
print("type(d):", type(d))

########################

print("Date.__dict__", Date.__dict__)
print("d.__dict__:", d.__dict__)

######################################

class X: 
    a = 10 
    b = 20 
    c = a + b 
    f = 3.14 
    L = [10, 20, 30, 40, 50]

print("X.__dict__:", X.__dict__)

print(X.a, X.b, X.c, X.f, X.L)
X.p = 100 
X.a = 100
del X.f 

objX = X()
print("type(objX):", type(objX))
print("objX.__dict__:", objX.__dict__)

class Y: 
    def test_func(): 
        print("In Y.test_func")

class Employee: 
    currentId = 0 
    def __init__(self, name): 
        self.name = name 
        self.empId = Employee.currentId + 1 

class Test: 
    def __init__(self): 
        print("In Test.__init__")

t = Test()
print("t.__dict__:", t.__dict__)

class Test: 
    def __init__(self): 
        self.a = 100 
        self.b = 200 
        self.c = 300 

t = Test() 
print(t.__dict__)

class Test: 
    def __init__(self, init_a, init_b, init_c): 
        self.a = init_a 
        self.b = init_b 
        self.c = init_c 

t = Test(100, 200, 300)

class Date: 
    def __init__(self, init_day, init_month, init_year): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year 

    def get_day(self): 
        return self.day 

    def set_day(self, new_day): 
        self.day = new_day 

