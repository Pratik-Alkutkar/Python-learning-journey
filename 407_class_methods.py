"""
class Test: 
    def f(): 
        print("In Test.f()")

t = Test() 
t.f() # Error 

# t.f() -> Test.f(t)
"""

# 0 parameters in bracket 

# 1 
class Test: 
    def f(self): 
        print("In Test.f(), id(self):", id(self))

t = Test() 
print("id(t):", id(t)) 
t.f() # t.f() == type(t).f(t) == Test.f(t)

# 2 
class Test: 
    def f(self): 
        print("In Test.f():id(self):", id(self))

t = Test() 
print("id(t):", id(t))
t.f() 
# t.f() == type(t).f(t) == Test.f(t)


# 3 
class Test: 
    def f(self): 
        print("In Test.f():id(self):", id(self))

t = Test() 
print("id(t):", id(t))
t.f()
# t.f() == type(t).f(t) == Test.f(t)

# 4 

class Test: 
    def f(self): 
        print("In Test.f():id(self):", id(self))
t = Test() 
print("id(t):", id(t))
t.f() 
# t.f() == type(t).f(t) == Test.f(t)

# 5 
class Test: 
    def f(self): 
        print("In Test.f():id(self):", id(self))
t = Test() 
print("id(t):", id(t))
t.f() 
# t.f() == type(t).f(t) == Test.f(t)

# 1 param in bracket 
# obj.f(p1)
print("One param in bracket")
# 1 
class Test: 
    def f(self, n): 
        print("In Test.f():id(self):", id(self))
        print("In Test.f():n:", n)
m = 500 
t = Test() 
print("id(t):", id(t))
t.f(m)
# t.f(m) == type(t).f(t, m) == Test.f(t, m) == Test.f(t, 500)

# 2 
class Test: 
    def f(self, n): 
        print("In Test.f():id(self):", id(self))
        print("In Test.f():n:", n)
m = 1000 
t = Test() 
print("id(t):", id(t))
t.f(m)
# t.f(m) == type(t).f(t, m) == Test.f(t, m) == Test.f(t, 1000)

# 3 
class Test: 
    def f(self, n): 
        print("In Test.f():id(self):", id(self)) 
        print("In Test.f():n", n)
m = 5000 
t = Test() 
print("id(t):", id(t))
t.f(m) 

# t.f(m) == type(t).f(t, m) == Test.f(t, m) == Test.f(t, 5000)

# 4 
class Test: 
    def f(self, n): 
        print("In Test.f():id(self):", id(self))
        print("In Test.f():n:", n)
m = 10000 
t = Test() 
print("id(t):", id(t))
t.f() 
# t.f(m) == type(t).f(t, m) == Test.f(t, m) == Test.f(t, 10000)

# 5 
class Test: 
    def f(self, n): 
        print("In Test.f():id(self):", id(self))
        print("In Test.f():n:", n)
m = 20000 
print("id(t):", id(t))
t.f() 
# t.f(m) == type(t).f(t, m) == Test.f(t, m) == Test.f(t, 20000)

# functions with 2 arguments in brack 

# 1 
class Test: 
    def g(self, m, n): 
        print("In Test.g():m=%d, n=%d" % (m, n)) 
t = Test() 
t.g(100, 200)
# t.g(100, 200) == type(t).g(t, 100, 200) == Test.g(t, 100, 200)

# 2 
class Test: 
    def g(self, m, n): 
        print("In Test.g():m = %d, n = %d" % (m ,n))
t = Test() 
t.g(1000, 2000)

# t.g(1000, 2000) == type(t).g(t, 1000, 2000) == Test.g(t, 1000, 2000)

# 3 
class Test: 
    def g(self, m, n): 
        print("In Test.g():m = %d, n = %d" % (m, n))
t = Test() 
t.g(50, 550) 
# t.g(50, 550) == type(t).g(t, 50, 550) == Test.g(t, 50, 550)

# 4 
class Test: 
    def g(self, m, n): 
        print("In Test.g():m = %d, n = %d" % (m ,n))
t = Test()
t.g() 
# t.g(-1, -2) == type(t).g(t, -1, -2) == Test(t, -1, -2)

# 5 
class Test: 
    def g(self, m, n): 
        print("In Test.g():m = %d, n = %d" % (m, n))
t = Test()
t.g(10000, 20000)
# t.g(10000, 20000) == type(t).g(t, 10000, 20000) == Test.g(t, 10000, 20000)
