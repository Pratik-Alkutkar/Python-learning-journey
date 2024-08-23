print("globals():", [v for v in globals().keys() if not v.startswith('__')])
import mypackage 
print("globals():", [v for v in globals().keys() if not v.startswith('__')])
print("type(mypackage):", type(mypackage))

print(mypackage.__dict__)
print("-----------------------------------------")
mypackage.__dict__['func']() 
mypackage.func() 

if id(mypackage.__dict__['func'] ) == id(mypackage.func): 
    print("SAME")

#-------------------------------------------------------------
print("Total internals method:")
globals()['mypackage'].__dict__['func']() # mypackage.func()

print("mypackage.N:", mypackage.N)
mypackage.N = 200
print("mypackage.N:", mypackage.N)