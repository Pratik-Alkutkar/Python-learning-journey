"""
5)  Let Test be a class and let t be its object containing attribute named 'n'. 
How will you prevent client from reassigning 'n' through the following syntax: 
t.n = rhs

Technique: Attribute management. 
Use any one one of the attr management technique. 
(preference: property)
"""

class Test: 
    def __init__(self, init_n): 
        self.__dict__['n'] = init_n 

    def getn(self): 
        return self.__dict__['n']
    
    def setn(self, rhs): 
        raise TypeError("Cannot reassign to 'n'")
    
    def deln(self): 
        del self.__dict__['n']

    n = property(getn, setn, deln)

t = Test(100)
print(t.n)
try: 
    t.n = 200 
except TypeError as e: 
    print(e)
print(t.__dict__)
del t.n 
print(t.__dict__)
