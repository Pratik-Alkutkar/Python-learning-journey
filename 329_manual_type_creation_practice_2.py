
#------------------------------------
cls_name = 'B1'
cls_bases = (object, )
cls_body = """
pass
"""
cls_dict = {} 
exec(cls_body, globals(), cls_dict)
B1 = type(cls_name, cls_bases, cls_dict)

cls_name = 'B2'
cls_bases = (object, )
cls_body = """
pass
"""
cls_dict = {} 
exec(cls_body, globals(), cls_dict)
B2 = type(cls_name, cls_bases, cls_dict)

cls_name = 'D'
cls_bases = (B1, B2)
cls_body = """
a = 10 
b = 20 
c = 30 
def __init__(self, init_n): 
    self.n = init_n 
def getn(self): 
    return self.n 
def setn(self, new_n): 
    self.n = new_n 
"""
cls_dict = {} 
exec(cls_body, globals(), cls_dict)
D = type(cls_name, cls_bases, cls_dict)

objD = D(100) 
print("type(objD):", type(objD))
print(objD.a, objD.b, objD.c, objD.getn())
print(D.__bases__)