# class to object 

# 1 
class X: 
	def __init__(self): 
		print("In X.__init__()")

x1 = X() 
x2 = X() 
x3 = X() 
# In X.__init__
# In X.__init__
# In X.__init__

print(x1.__dict__) # {} 
print(x2.__dict__) # {}
print(x3.__dict__) # {} 
print(X.__dict__) # {'__init__' : function object}

#2 
class X1: 
	pass 

x = X1() 
# class namespace : ClassName.__dict__
print("X1.__dict__:", X1.__dict__) # Only built in attributes:value 

# object namespace : ObjectName.__dict__ 
print("x.__dict__:", x.__dict__) # {} 

# 3 
class X3: 
	pass 

x = X3() 
# Class Namespace : ClassName.__dict__ 
print("X3.__dict__:", X3.__dict__)
# Object Namespace: ObjectName.__dict__ 
print("x.__dict__:", x.__dict__)

# 4 
class X4: 
	pass 

x = X4() 
# Class Namespace: ClassName.__dict__ 
print("X4.__dict__:", X4.__dict__)
# Object Namespace : ObjectName.__dict__ 
print("x.__dict__:", x.__dict__)

# 5 

class X5: 
	pass 

x = X5() 
# Class Namespace: ClassName.__dict__ 
print("X5.__dict__:", X5.__dict__)
# Object Namespace : ObjectName.__dict__ 
print("x.__dict__:", x.__dict__)
