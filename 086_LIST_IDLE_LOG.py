Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C = """LIST DATA TYPE"""
C = """Ways of Creation"""
L = [10, 20, 30, 40, 50]
# constructor method
s = "Hello"
T = (10, 20, 30, 40, 50, 60)
S = {-100, -200, -300}
L1 = list(s)
L2 = list(T)
L3 = list(S)
print(L1, L2, L3)
['H', 'e', 'l', 'l', 'o'] [10, 20, 30, 40, 50, 60] [-200, -300, -100]
print(type(L1), type(L2), type(L3))
<class 'list'> <class 'list'> <class 'list'>
# list comprehension
L = [x**2 for x in range(1, 51)]
L
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500]
L = [x**2 for x in range(1, 51) if x % 2 == 0]
L
[4, 16, 36, 64, 100, 144, 196, 256, 324, 400, 484, 576, 676, 784, 900, 1024, 1156, 1296, 1444, 1600, 1764, 1936, 2116, 2304, 2500]
C = """Built in functions"""
L = [10, 20, 30, 40]
print(L)
[10, 20, 30, 40]
type(L)
<class 'list'>
id(L)
2674536741952
len(L)
4
C = """Built in operators"""
L1=[10, 20, 30, 40, 50]
L2=[60, 70, 80, 90, 100]
L3 = L1 + L2 # Concat
L4 = L1 * 4 # Multiplication by integer
L3
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
L4
[10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
# index
for i in range(len(L1)):
    print(i, L1[i])

    
0 10
1 20
2 30
3 40
4 50
L4
[10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
# range, slice, positive, negative indexing, positive negative step count, anchor
L4[:6]
[10, 20, 30, 40, 50, 10]
L[8:]
[]
L4[8:]
[40, 50, 10, 20, 30, 40, 50, 10, 20, 30, 40, 50]
L4[2 : 10]
[30, 40, 50, 10, 20, 30, 40, 50]
L4[-10:-1]
[10, 20, 30, 40, 50, 10, 20, 30, 40]
L4[::-1]
[50, 40, 30, 20, 10, 50, 40, 30, 20, 10, 50, 40, 30, 20, 10, 50, 40, 30, 20, 10]
L4[1::2]
[20, 40, 10, 30, 50, 20, 40, 10, 30, 50]
L4[::2]
[10, 30, 50, 20, 40, 10, 30, 50, 20, 40]
L[4:9]
[]
L4[4:9]
[50, 10, 20, 30, 40]
L4[8:3:-1]
[40, 30, 20, 10, 50]
L4[-10:-1:2]
[10, 30, 50, 20, 40]
L4[-1:-10:-2]
[50, 30, 10, 40, 20]
# index method
L=[10,20,30,10,40,50,60,70,10,80,90,100,10,110,120]
L.index(10)
0
L.index(10, 1)
3
L.index(10, 4)
8
L.index(-5)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    L.index(-5)
ValueError: -5 is not in list
# count method
L.count(10)
4
L.count(20)
1
L.count(-5)
0
# member ship teseting
10 in L
True
-5 in L
False
# common to list and str
# L1 + L2, L * n, L[i], L[i:j], L[i:j:k], member in L, L.index(element), L.index(element, search_index), L.count(element)
# List can be modified in three ways, Add new elements, remove existing elements, replace existing elements
L = []
L.append(10)
L.append(True)
L
[10, True]
L.append(3.14)
s = "Hello"
L.append(s)
L
[10, True, 3.14, 'Hello']
T = (-1, -2, -3)
L.append(T)
L
[10, True, 3.14, 'Hello', (-1, -2, -3)]
D = {'a':1000, 'b':2000}
L.append(D)
L
[10, True, 3.14, 'Hello', (-1, -2, -3), {'a': 1000, 'b': 2000}]
S = {18, 29, 38}
L.append(S)
L
[10, True, 3.14, 'Hello', (-1, -2, -3), {'a': 1000, 'b': 2000}, {18, 29, 38}]
