Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Parameter passing mechanisms
# 1 Positional parameters
def test(a, b, c):
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))

    
test(10, 20, 30)
10 <class 'int'>
20 <class 'int'>
30 <class 'int'>
type('a', 'b', 'c')
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type('a', 'b', 'c')
TypeError: type.__new__() argument 2 must be tuple, not str
test('a', 'b', 'c')
a <class 'str'>
b <class 'str'>
c <class 'str'>
test(True, 10, 3.14)
True <class 'bool'>
10 <class 'int'>
3.14 <class 'float'>
test(10, 20)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    test(10, 20)
TypeError: test() missing 1 required positional argument: 'c'
test(10, 20, 30, 40)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    test(10, 20, 30, 40)
TypeError: test() takes 3 positional arguments but 4 were given
# 2: keyword arguments
def test(a, b, c, d, e):
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(e, type(e))

    
test(a=10, b=20, c=30, d=40, e=50)
10 <class 'int'>
20 <class 'int'>
30 <class 'int'>
40 <class 'int'>
50 <class 'int'>
test(e=50, c=30, b=20, a=10, d=40)
10 <class 'int'>
20 <class 'int'>
30 <class 'int'>
40 <class 'int'>
50 <class 'int'>
# Mixing non-keyword and keyword syntax!
test(10, 20, c=30, d=40, e=50)
10 <class 'int'>
20 <class 'int'>
30 <class 'int'>
40 <class 'int'>
50 <class 'int'>
test(10, 20, e=50, c=30, d=40)
10 <class 'int'>
20 <class 'int'>
30 <class 'int'>
40 <class 'int'>
50 <class 'int'>
test(10, 20, c=30, d=40, 50)
SyntaxError: positional argument follows keyword argument
# 3. Extra nonkeyword argument
def test(X):
    print(X, type(X))

    
test(10)
10 <class 'int'>
L = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
test(L)
[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000] <class 'list'>
print()

print(10)
10
print(10, 20)
10 20
print(10, 20, 30)
10 20 30
print("Hello", (10, 20, 30), [100, 200, 300])
Hello (10, 20, 30) [100, 200, 300]
print(1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e')
1 2 3 4 5 a b c d e
def my_print(obj, sep, end):
    print(obj, sep, end)

    
my_print()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    my_print()
TypeError: my_print() missing 3 required positional arguments: 'obj', 'sep', and 'end'
def test(X):
    print(X)

    
test()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    test()
TypeError: test() missing 1 required positional argument: 'X'
test()
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    test()
TypeError: test() missing 1 required positional argument: 'X'
test(10, 20, 30)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    test(10, 20, 30)
TypeError: test() takes 1 positional argument but 3 were given
test(10, 20, 30, 40)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    test(10, 20, 30, 40)
TypeError: test() takes 1 positional argument but 4 were given
def test(*args):
    print(args, type(args))

    
test()
() <class 'tuple'>
test(10, 20)
(10, 20) <class 'tuple'>
test(10, 20, 30, 40)
(10, 20, 30, 40) <class 'tuple'>
test("Hello", (100, 200, 300), [1.1, 2.2, 3.3])
('Hello', (100, 200, 300), [1.1, 2.2, 3.3]) <class 'tuple'>
test(10, 20, 30, 40, 50, 'a', 'b', 'c' , 'd', 'e')
(10, 20, 30, 40, 50, 'a', 'b', 'c', 'd', 'e') <class 'tuple'>
T = (10)
type(T)
<class 'int'>
T = (10, )
type(T)
<class 'tuple'>
10
10
(10)
10
type((10,))
<class 'tuple'>
type((10))
<class 'int'>
test(10)
(10,) <class 'tuple'>
T = (10, )
T
(10,)
def test(*args):
    print(args, type(args))

    
test(10, 20, 30)
(10, 20, 30) <class 'tuple'>
test(*(10, 20, 30))
(10, 20, 30) <class 'tuple'>
T = (10, 20, 30)
test(*T)
(10, 20, 30) <class 'tuple'>
test(T)
((10, 20, 30),) <class 'tuple'>
def func(X):
    print(X)

    
func(T)
(10, 20, 30)
def test(*args):
    print(args, type(args))

    
test(10, 20, 30)
(10, 20, 30) <class 'tuple'>
test(10, 20, 30)
(10, 20, 30) <class 'tuple'>
test(10, 20, 30)
(10, 20, 30) <class 'tuple'>
test(*(10, 20, 30))
(10, 20, 30) <class 'tuple'>
t
test(*(10, 20, 30))
(10, 20, 30) <class 'tuple'>
test(*(10, 20, 30))
(10, 20, 30) <class 'tuple'>

T = (10, 20, 30)
test(*T)
(10, 20, 30) <class 'tuple'>
T = (10, 20, 30)
test(*T)
(10, 20, 30) <class 'tuple'>
T = (10, 20, 30)
test(*T)
(10, 20, 30) <class 'tuple'>
(10, 20, 30)
(10, 20, 30)
# 6: Extra keyword arguments
def test(**kwargs):
    print(kwargs, type(kwargs))

    
def test(10):
    
SyntaxError: invalid syntax
def test(3.14):
    
SyntaxError: invalid syntax
def test(X):
    print(X)

    
def test(*X):
    print(X)

    
test(10)
(10,)
def test_1(X):print(X)

def test_2(*X):print(X)

test_1(10)
10
test_1([10, 20, 30, 40])
[10, 20, 30, 40]
test_2(10, 20, 30, 40)
(10, 20, 30, 40)
def test(**kwargs):
    print(kwargs, type(kwargs))

    
test(a=10, b=20, c=30, d=40)
{'a': 10, 'b': 20, 'c': 30, 'd': 40} <class 'dict'>
