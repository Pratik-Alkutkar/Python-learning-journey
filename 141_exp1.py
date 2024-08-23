class B1:pass 
class B2:pass 
class B3:pass 
class B4:pass 

class D1(B1, B2):pass 
class D2(B3, B4):pass 

class D(D1,D2):pass 

print("D.__mro__:", D.__mro__)
print("D1.__mro__:", D1.__mro__)
print("D2.__mro__:", D2.__mro__)