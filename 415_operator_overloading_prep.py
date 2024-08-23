import sys 

class X: 
    pass 

x1 = X() 
x2 = X() 
print("type(x1):{}, type(x2):{}".format(type(x1), type(x2)))

try: 
    rs = x1 + x2 
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data)

try:
    rs = x1 - x2 
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data) 

try: 
    rs = x1 * x2 
except: 
    exc_name, exc_data, _ = sys.exc_info()
    print(exc_name, exc_data)

try: 
    rs = x1 // x2 
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data)
    
    
try: 
    rs = x1 % x2 
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data)


try: 
    rs = x1 << x2 
except: 
    exc_name, exc_data, _ = sys.exc_info() 
    print(exc_name, exc_data)
