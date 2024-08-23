#--------------------------------------------
num = 100 
print("globals():", globals())
def test_function(): 
    print("locals():", locals())
    num = 200 
    print("locals():", locals())
test_function()
print("globals():", globals())
#--------------------------------------------
num = 100 
def test_func(): 
    num = 200 
print("num:",num) # 100 
test_func() 
print("num:", num) # 100
#--------------------------------------------
print("global statement effect proof")
N = 100 
def test(): 
    global N 
    print("locals():", locals()) # {} 
    N = 200 
    print(N)
    print("locals():", locals()) # {} 

print("globals():", globals()) # N:100
test()
print("globals():", globals()) # N:200
#--------------------------------------------