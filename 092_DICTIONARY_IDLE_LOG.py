Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C = """Dictionary Data Type"""
# Ways of creation
# explicity syntax
D = {True: 100, 10:200, 3.14:300, 'Hello':400, (1,2,3): 500}
D[True]
100
D[10]
200
D[3.15]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    D[3.15]
KeyError: 3.15
D[3.14]
300
D['Hello']
400
D[(1,2,3)]
500
# constructor method
D = dict(name='Pratik', mob=000, city='Pune')
D
{'name': 'Pratik', 'mob':000 ,'city': 'Pune'}
# fromkeys method
K = ['a', 'b', 'c']
D = dict.fromkeys(K)
print(D)
{'a': None, 'b': None, 'c': None}
D['a'] = 10
D
{'a': 10, 'b': None, 'c': None}
D['b'] = 20
D
{'a': 10, 'b': 20, 'c': None}
D['c'] = 30
D
{'a': 10, 'b': 20, 'c': 30}
D1 = dict.fromkeys(K, 0)
D1
{'a': 0, 'b': 0, 'c': 0}
# dict(zip(K, V))
K=['a', 'b', 'c']
V=[10, 20, 30]
z = zip(K, V)
type(z)
<class 'zip'>
for x in z:
    print(x)

    
('a', 10)
('b', 20)
('c', 30)
z = zip(K, V)
emp_ids = [10, 20, 25, 30, 35]
emp_names = ['Pratik', 'Rohit', 'Ashish', 'Radhika', 'Sneha']
emp_cities = ['Pune', 'Ichalkaranji', 'Pune', 'Mumbai', 'Nashik']
emp_sal = [10000, 20000, 30000, 40000, 50000]
z = zip(emp_ids, emp_names, emp_cities, emp_sal)
for x in z:
    print(x)

    
(10, 'Pratik', 'Pune', 10000)
(20, 'Rohit', 'Ichalkaranji', 20000)
(25, 'Ashish', 'Pune', 30000)
(30, 'Radhika', 'Mumbai', 40000)
(35, 'Sneha', 'Nashik', 50000)
z = zip(K, V)
D = dict(z)
D
{'a': 10, 'b': 20, 'c': 30}
dict(zip([10, 20, 30], [1.1, 2.2, 3.3]))
{10: 1.1, 20: 2.2, 30: 3.3}
C = """Built in functions"""
print(D)
{'a': 10, 'b': 20, 'c': 30}
len(D)
3
type(D)
<class 'dict'>
id(d)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    id(d)
NameError: name 'd' is not defined. Did you mean: 'D'?
id(D)
2049046540736
C = """Class methods"""
# Views of dictionary
D = {'a':100, 'b':200, 'c':300, 'd':400}
K = D.keys()
print(KK)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(KK)
NameError: name 'KK' is not defined. Did you mean: 'K'?
print(K)
dict_keys(['a', 'b', 'c', 'd'])
for key in D.keys():
    print(key, D[key])

    
a 100
b 200
c 300
d 400
V = D.values()
type(V)
<class 'dict_values'>
for val in V:
    print(val)

    
100
200
300
400
I = D.items()
type(I)
<class 'dict_items'>
for item in I:
    print(item)

    
('a', 100)
('b', 200)
('c', 300)
('d', 400)
L1 = [10, 20, 30, 40]
for x in L1:
    print(x)

    
10
20
30
40
L2 = [(1,2,3), (4,5,6), (7,8,9), (10,11,12)]
for x in L2:
    print(x)

    
(1, 2, 3)
(4, 5, 6)
(7, 8, 9)
(10, 11, 12)
for x in L2:
    print(x[0], x[1], x[2])

    
1 2 3
4 5 6
7 8 9
10 11 12
for (x, y, z) in L2:
    print(x, y, z)

    
1 2 3
4 5 6
7 8 9
10 11 12
D.items()
dict_items([('a', 100), ('b', 200), ('c', 300), ('d', 400)])
for (key, val) in D.items():
    print(key, val)

    
a 100
b 200
c 300
d 400
# Explorting mutablility of dictionary
# How to add, edit and remove key:value pair ?
# Add: D[new_key] = some_val (new_key:some_value pair will be added in dict)
# Edit/Modify: D[existing_key] = new_value (existing key will give up existing
# value and will accept new_value in the SAME item)
# Remove/delete: del D[existing_key]
# existing_key:value pair will be removed from dict
D
{'a': 100, 'b': 200, 'c': 300, 'd': 400}
D['x'] = 500
D
{'a': 100, 'b': 200, 'c': 300, 'd': 400, 'x': 500}
D['c']=600
D
{'a': 100, 'b': 200, 'c': 600, 'd': 400, 'x': 500}
del D['x']
D
{'a': 100, 'b': 200, 'c': 600, 'd': 400}
D['a']
100
del D['b']
D
{'a': 100, 'c': 600, 'd': 400}
D['x']
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    D['x']
KeyError: 'x'
del D['x']
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    del D['x']
KeyError: 'x'
D
{'a': 100, 'c': 600, 'd': 400}
D.popitem()
('d', 400)
D
{'a': 100, 'c': 600}
D = {'a':10, 'b':20, 'c':30, 'd':40}
t = D.popitem()
t
('d', 40)
D
{'a': 10, 'b': 20, 'c': 30}
n = D.pop('a')
n
10
D
{'b': 20, 'c': 30}
D['b']
20
D.get('b')
20
D['x']
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    D['x']
KeyError: 'x'
D.get('x')
ret = D.get('x')
print(ret)
None
D
{'b': 20, 'c': 30}
D['x'] = None
D
{'b': 20, 'c': 30, 'x': None}
D.get(x)
D.get('x')
x
10
D.get(500)
D.get('x')
500 in D.keys()
False
'x' in D.keys()
True
D.get(4000, -1)
-1
