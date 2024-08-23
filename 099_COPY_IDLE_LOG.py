Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C = """Detailed explanation of copy() semnatics in Python"""
L1 = [10, 20, 30]
id(L1)
2600841176832
L2 = L1
id(L1)
2600841176832
id(L2)
2600841176832
L1 == L2
True
L3 = L1.copy()
id(L1)
2600841176832
id(L3)
2600841386368
L3
[10, 20, 30]
id(L1) != id(L3)
True
L1 == L3
True
L = []
id(L)
2600841385728
def test_func(lst):
    print("id(lst):", lst)

    
test_func(L)
id(lst): []
def test_func(lst):
    print("id(lst):", id(lst))

    
test_func(L)
id(lst): 2600841385728
def test_func(X):
    print("id(X):", id(X))

    
s = "Hello"
id(s)
2600841316144
test_func(s)
id(X): 2600841316144
L = [100, 200, 300]
L
[100, 200, 300]
######################################
C="""L.copy() makes copy for top level elements"""
L1 = [10, 20, 30]
L2 = L1.copy()
L3 = [100, 200, 300, [400, 500, 600]]
L4 = L3.copy()
id(L1)
2600841310976
id(L2)
2600841317952
L1==L2
True
L3==L4
True
id(L3)
2600840197440
id(L4)
2600841317824
for x in L1:
    print(x, id(x))

    
10 2600803828240
20 2600803828560
30 2600803828880
for x in L2:
    print(x, id(x))

    
10 2600803828240
20 2600803828560
30 2600803828880
for x in L3:
    print(x, id(x))

    
100 2600803831120
200 2600803834320
300 2600839803184
[400, 500, 600] 2600841315008
for x in L4:
    print(x, id(x))

    
100 2600803831120
200 2600803834320
300 2600839803184
[400, 500, 600] 2600841315008
L3
[100, 200, 300, [400, 500, 600]]
L3[3]
[400, 500, 600]
L3[3].append(700)
L4
[100, 200, 300, [400, 500, 600, 700]]
C = """Full fledged deep copy"""
L5 = [1000, 2000, 3000, [4000, 5000, 6000]]
import copy
L6 = copy.deepcopy(L5)
id(L5)
2600841329024
id(L6)
2600841387008
L5==L6
True
L5
[1000, 2000, 3000, [4000, 5000, 6000]]
L6
[1000, 2000, 3000, [4000, 5000, 6000]]
for x in L5:
    print(x, id(x))

    
1000 2600839801136
2000 2600839801040
3000 2600839801104
[4000, 5000, 6000] 2600841384064
for x in L6:
    print(x, id(x))

    
1000 2600839801136
2000 2600839801040
3000 2600839801104
[4000, 5000, 6000] 2600841387264
L5[3].append(7000)
L5
[1000, 2000, 3000, [4000, 5000, 6000, 7000]]
L6
[1000, 2000, 3000, [4000, 5000, 6000]]
C = """Remarks for C++ programmers"""
C = """
v1 = mutable_object
v2 = v1 # Shallow copy
v2 = copy.deepcopy(v1) # True deep copy
v2 = v1.copy() # shallow version of deep copying, (shallow version of deep copy = true deep copy if v1 contains all immutables
"""
