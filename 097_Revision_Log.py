Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Revision of dictionary methods
D = {'a': 10, 'b': 20, 'c': 30}
D = dict(a=10, b=20, c=30)
K=['a', 'b', 'c']
D = dict.fromkeys(K)
D
{'a': None, 'b': None, 'c': None}
D = dict.fromkeys(K, 0)
K = ['a', 'b', 'c']
V = [10, 20, 30]
dict(zip(K, V))
{'a': 10, 'b': 20, 'c': 30}
for key in D.keys(): print(key)

a
b
c
for v in D.values(): print(v)

0
0
0
for t in D.items(): print(t)

('a', 0)
('b', 0)
('c', 0)
for (k, v) in D.items(): print(k, v)

a 0
b 0
c 0
D
{'a': 0, 'b': 0, 'c': 0}
D['x'] = 100
D
{'a': 0, 'b': 0, 'c': 0, 'x': 100}
del D['x']
D
{'a': 0, 'b': 0, 'c': 0}
D['a'] = 100
D
{'a': 100, 'b': 0, 'c': 0}
D['b'] = 200
D
{'a': 100, 'b': 200, 'c': 0}
D['c'] = 300
D
{'a': 100, 'b': 200, 'c': 300}
D
{'a': 100, 'b': 200, 'c': 300}
n = D.pop('a')
n
100
D
{'b': 200, 'c': 300}
T = D.popitem()
D
{'b': 200}
D
{'b': 200}
T
('c', 300)
D.clear()
D
{}
D = {'a':10, 'b':20, 'c':30}
D['a']
10
D.get('a')
10
D['x']
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    D['x']
KeyError: 'x'
D.get('x')
