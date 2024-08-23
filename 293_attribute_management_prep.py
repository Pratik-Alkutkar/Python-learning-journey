import sys 

class Test: 
    def __init__(self, init_n): 
        self.n = init_n 


t = Test(100)

# RHS 
print("rhs") # rhs 
m = t.n 
print(m) # 100 

print("lhs") # lhs 
t.n = 200 

print("rhs") # rhs 
m = t.n 
print(m) #200 

print("del") # del 
del t.n 

try: 
    print(t.n)
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data) # exc_name, exc_info
 

