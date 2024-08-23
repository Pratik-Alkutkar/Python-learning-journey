Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C = """Dictionary methods continued..."""
D1 = {'a':10, 'b':20, 'c':30, 'd':40}
D2 = {'c':30, 'd':40, 'e':50, 'f':60}
D2 = {'c':300, 'd':400, 'e':500, 'f':600}
D1
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
D2
{'c': 300, 'd': 400, 'e': 500, 'f': 600}
D1.update(D2)
D1
{'a': 10, 'b': 20, 'c': 300, 'd': 400, 'e': 500, 'f': 600}
D1 = {'a':10, 'b':20, 'c':30, 'd':40}
D2 = {'c':300, 'd':400, 'e':500, 'f':600}
D1
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
D
2
2
D1
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
D2
{'c': 300, 'd': 400, 'e': 500, 'f': 600}
D2.update(D1)
D1
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
D2
{'c': 30, 'd': 40, 'e': 500, 'f': 600, 'a': 10, 'b': 20}
# UpDate method finished here
# setdefault
D
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    D
NameError: name 'D' is not defined. Did you mean: 'D1'?
D = {'a':10, 'b':20, 'c':30, 'd':40}
D['a']
10
D.get('a')
10
D.setdefault('a')
10
D['a']
10
D['x']
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    D['x']
KeyError: 'x'
D.get('x')
D
{'a': 10, 'b': 20, 'c': 30, 'd': 40}
D.setdefault('x')
D
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'x': None}
D.setdefault('y', 500)
500
D
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'x': None, 'y': 500}
dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
