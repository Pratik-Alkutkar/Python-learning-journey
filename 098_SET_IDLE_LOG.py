Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C = """Set data type"""
# ways of creation
# Rule: Set can contain only immutable objects
# Def: Set: Set is an unordered collection without repetitions
# Internal Knowledge: Internally set is implemented as a wrapper around dict_keys.
C = """Ways of creation"""
S = {True, 10, 3.14, "Hello", (10, 20, 30)}
print(S)
{True, 3.14, 'Hello', 10, (10, 20, 30)}
type(S)
<class 'set'>
S = { {1, 2, 3} }
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    S = { {1, 2, 3} }
TypeError: unhashable type: 'set'
S = { [10, 20, 30, 40] }
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    S = { [10, 20, 30, 40] }
TypeError: unhashable type: 'list'
S = { {'a' : 10, 'b': 20} }
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    S = { {'a' : 10, 'b': 20} }
TypeError: unhashable type: 'dict'
# empty set syntax
S = {} # S will be a dictionary because type inference algorithm {} -> dict
type(S)
<class 'dict'>
S = set()
print(S)
set()
type(S)
<class 'set'>
s = "aaabbbCCCddEEE"
L = [10, 20, 30, 10, 40, 20, 20, 10, 40, 30]
S1 = set(s)
S2 = set(L)
print(S1)
{'d', 'b', 'E', 'C', 'a'}
print(S2)
{40, 10, 20, 30}
C = """Builts functions on Set S"""
S = {10, 20, 30, 40}
S
{40, 10, 20, 30}
print(S)
{40, 10, 20, 30}
id(S)
1957460988128
type(S)
<class 'set'>
len(S)
4
C = """Methods on set"""
S1 = {10, 20, 30, 40}
S2 = {30, 40, 50, 60}
S1.union(S2)
{40, 10, 50, 20, 60, 30}
S1
{40, 10, 20, 30}
S2
{40, 50, 60, 30}
S1.intersection(S2)
{40, 30}
S1
{40, 10, 20, 30}
S2
{40, 50, 60, 30}
S3 = S1.union(S2)
S3
{40, 10, 50, 20, 60, 30}
rs = S1.intersection(S2)
print(rs)
{40, 30}
rs = S1.difference(S2)
print(rs)
{10, 20}
rs = S2.difference(S1)
print(rs)
{50, 60}
rs = S1.symmetric_difference(S2)
print(rs)
{10, 50, 20, 60}
rs = S2.symmetric_difference(S1)
rs
{10, 50, 20, 60}
S1.update(S2) # S1 is updated by S1 union S2
S2
{40, 50, 60, 30}
S1
{40, 10, 50, 20, 60, 30}
S1 = {10, 20, 30, 40}
S1.intersection_update(S2) # S1 is updated by S1 intersection S2
S2
{40, 50, 60, 30}
S1
{40, 30}
S1 = {10, 20, 30, 40}
S1
{40, 10, 20, 30}
S2
{40, 50, 60, 30}
S2.intersection_update(S1) # S2 is updated by S2 intersection S1
S1
{40, 10, 20, 30}
S2
{40, 30}
S2 = {20, 30, 40, 50}
S1
{40, 10, 20, 30}
S2
{40, 50, 20, 30}
S1
{40, 10, 20, 30}
S2
{40, 50, 20, 30}
S1.difference_update(S2) # S1 is updated by S1-S2
S1
{10}
S2
{40, 50, 20, 30}
S1 = {10, 20, 30, 40}
S2 = {30, 40, 50, 60}
S1.difference_update(S2) # S1 is updated by S1-S2
S1
{20, 10}
S2
{40, 50, 60, 30}
S1 = {10, 20, 30, 40}
S1.symmetric_difference_update(S2) # S1 is updated by symmetric difference of S1 and S2
S1
{10, 50, 20, 60}
S2
{40, 50, 60, 30}
# subset
S1 = {10, 20, 30}
S2 = {10, 20, 30, 40, 50}
S1.issubset(S2)
True
S1.issubset(S2)
True
S1.issubset(S1)
True
S1.issuperset(S2)
False
S2.issuperset(S1)
True
S1.issuperset(S1)
True
# add/remove
S = set()
S
set()
S.add(True)
S
{True}
S.add(10)
S
{True, 10}
S.add(3.14)
S
{True, 10, 3.14}
S.add("Hello")
S
{True, 10, 3.14, 'Hello'}
S.add((10, 20, 30))
S
{True, 3.14, 10, (10, 20, 30), 'Hello'}
S.add([100, 200, 300, 400]_)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
S.add([100, 200, 300, 400])
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    S.add([100, 200, 300, 400])
TypeError: unhashable type: 'list'
S
{True, 3.14, 10, (10, 20, 30), 'Hello'}
S.remove(True)
S
{3.14, 10, (10, 20, 30), 'Hello'}
S.remove(10)
S
{3.14, (10, 20, 30), 'Hello'}
S.remove(3.14)
S.remove(500)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    S.remove(500)
KeyError: 500
S.discard(500)
S
{(10, 20, 30), 'Hello'}
S
{(10, 20, 30), 'Hello'}
S = {10, 20, 30, 40, 50}
print(S)
{50, 20, 40, 10, 30}
x = S.pop()
x
50
S
{20, 40, 10, 30}
S.pop()
20
S
{40, 10, 30}
S.pop()
40
S.pop()
10
S.pop()
30
S
set()
S = {100, 200, 300}
S.clear()
S
set()
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
S1 = {10, 20, 30}
S2 = {30, 40, 50}
S3 = {40, 50, 60}
S1.isdisjoint(S2)
False
S1.isdisjoint(S2)
False
