Combinations not involving extra-nonkeyword argument

1) Positional + Keyword
def test(a, b, c, d, e):
    pass

2) Positional + default
def test(a, b, c, d=100, e=200):
    pass

3) Default + Extra-keyword
def test(a=10, b=20, **kwargs):
    pass

4) Positional/Keyword + default + Extra-keyword

def test(a, b, c, d=100, e=200, **kwargs):
    print(a, b, c) # by poistion / by keyword
    print(d, e) # override the default using keyword syntax or keep default
    print(kwargs) # extra keyword arguments

#-------------------------------------------------------------------------
Combinations involving extra-nonkeyword

1) Positional + extra-non-keyword
def test(a, b, c, *args):
    print(a, b, c) # matched by position
    print(args) # extra non-keyword argument

2) extra-nonkeyword + keyword only
def test(*args, p, q):
    print(args)
    print(p, q)

3) extra-nonkeyword + default
def test(*args, a=100, b=200):
    print(args)
    print(a, b)

4) extra-nonkeyword + default + keyword only
def teset(*args, a=100, b=200, p, q):
    print(args)
    print(a, b)
    print(p, q)

5) extra-nonkeyword + default + keyword only + extra-keyword
def test(*args, d=100, e=200, p, q, **kwargs):
    print(args) # extranonkeyword
    print(d, e) # default
    print(p, q) # keyword only
    print(kwargs) # extra keyword

6) Pos + extra-nonkeyword + default + keyword only + extra keyword
def test(a, b, c, *args, d=100, e=200, p, q, **kwargs):
    print(a, b, c) # Pos
    print(args) # extra-nonkeyword
    print(d, e) # default
    print(p, q) # keyword only
    print(kwargs) # extra keyword

#-----------------------------------------------------------

    



    
    
