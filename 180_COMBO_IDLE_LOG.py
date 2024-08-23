Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Combining different types of formal parameters
def test(a, b, c, d, e):
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(d, type(d))
    print(e, type(e))

    
test(10, 20, e=50, c=30, d=40) # Positional + keyword arguments. a, b, -> matched by position, c, d, e-> matched by keyword
10 <class 'int'>
20 <class 'int'>
30 <class 'int'>
40 <class 'int'>
50 <class 'int'>
# Positional + Extra-nonkeyword
def test(a, b, c, *args):
    print(a, b, c)
    print(args)

    
test(10, 20, 30, 100, 200, 300, 400, 500) # a, b, c-> matched by position, rest are absorbed by args
10 20 30
(100, 200, 300, 400, 500)
test(10, 20, 30, 1.1, 2.2, 3.3)
10 20 30
(1.1, 2.2, 3.3)
# position/keyword + default
def test(a, b, c, d=100, e=200):
    print(a, b, c)
    print(d, e)

    
test(1, 2, 3)
1 2 3
100 200
test(a=1, b=2, c=3)
1 2 3
100 200
test(1, 2, 3, e=-200)
1 2 3
100 -200
test(a=1, b=2, c=3, e=-200)
1 2 3
100 -200
test(10, 20, c=-30, e=-200)
10 20 -30
100 -200
# you cannot write non-default after default
def teset(a, b, c, d=100, e=200, f, g):
    
SyntaxError: non-default argument follows default argument
# default + extra keyword
def test(a=100, b=200, **kwargs):
    print(a, b)
    print(kwargs)

    
test()
100 200
{}
test(b=-200, p=1.1, q=2.2)
100 -200
{'p': 1.1, 'q': 2.2}
# Positional + Default + Extra-keyword
def test(a, b, c, d=100, e=200, **kwargs):
    print(a, b, c)
    print(d, e)
    print(kwargs)

    
test(1, 2, 3, e=200, p=1.1, q=2.2)
1 2 3
100 200
{'p': 1.1, 'q': 2.2}
