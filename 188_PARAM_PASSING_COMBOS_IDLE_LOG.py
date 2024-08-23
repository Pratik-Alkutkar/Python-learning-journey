Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# All parameter passing combinations revised
# 1) Pos + Keyword
def test(a, b, c, d, e):
    print(a, b, e, d, e)

    
test(10, 20, e=50, c=30, d=40) # a, b -> Pos, c,d,e->keyword
10 20 50 40 50
# 2) Pos/keyword + default
def test(a, b, c, d=100, e=200):
    print(a, b, c) # Pos
    print(d, e) # Default

    
test(10, 20, 30)
10 20 30
100 200
test(10, 20, 30, e=-200)
10 20 30
100 -200
# 3) default + extra keyword
def test(d=100, e=200, **kwargs):
    print(d, e) # default
    print(kwargs) # extra keyword

    
test(e=-200, p=1.1, q=2.2, r=3.3)
100 -200
{'p': 1.1, 'q': 2.2, 'r': 3.3}
# 4) Pos/keyword + default + extra keyword
def test(a, b, c, d=100, e=200, **kwargs):
    print(a, b, c) # Pos / keyword
    print(d, e) # default
    print(kwargs) # extra keyword

    
test(10, 20, 30, e=-200, p=1.1, q=2.2, r=3.3)
10 20 30
100 -200
{'p': 1.1, 'q': 2.2, 'r': 3.3}
test(10, 20, c=30, e=-200, p=1.1, q=2.2, r=3.3)
10 20 30
100 -200
{'p': 1.1, 'q': 2.2, 'r': 3.3}
# Combinations involving extra nonkeyword argument
# 1) Pos + extra nonkeyword
def test(a, b, *args):
    print(a, b) # Pos
    print(args) # extra nonkeyword

    
test(10, 20, 30, 40, 50, 60 ,70)
10 20
(30, 40, 50, 60, 70)
# 2) extra-nonkeyword + default
def test(*args, d=100, e=200):
    print(args) # extra nonkeyword
    print(d, e) # default

    
test(10, 20, 30, 40, 50, e=-200)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    est(10, 20, 30, 40, 50, e=-200)
NameError: name 'est' is not defined. Did you mean: 'test'?
test(10, 20, 30, 40, 50, e=-200)
(10, 20, 30, 40, 50)
100 -200
# 3) extra-nonkeyword + keyword only
def test(*args, p, q):
    print(args) # extra nonkeyword
    print(p, q) # keyword only

    
test(10, 20, 30, 40, p=1.1, q=2.2)
(10, 20, 30, 40)
1.1 2.2
# 4) extra-nonkeyword + default + keyword only
def test(*args, d=100, e=200, p, q):
    print(args) # extra nonkeyword
    print(d, e) # default
    print(p, q) # keyword only

    
test(10, 20, 30, 40, e=-200, p=1.1, q=2.2)
(10, 20, 30, 40)
100 -200
1.1 2.2
# 5) Pos + extra non-keyword + default

def test(a, b, c, *args, d=100, e=200):
    print(a, b, c) # pos
    print(args) # extra keyword
    print(d, e) # default

    
test(10, 20, 30, 40, 50, 60, 70, e=-200)
10 20 30
(40, 50, 60, 70)
100 -200
# 5) Pos + extra-nonkeyword + keyword only
def test(a, b, c, *args, p, q):
    print(a, b, c) # Pos
    print(args) # extra nonkeyword
    print(p, q) # keyword only

    
test(10, 20, 30, *(40, 50, 60), p=1.1, q=2.2)
10 20 30
(40, 50, 60)
1.1 2.2
# 6) Pos + extra nonkeyword + default + keyword only + extra keyword

def master_function(a, b, c, *args, d=100, e=-200, p, q, **kwargs):
    print("Positional arguments:")
    print("a:{}, b:{}, c:{}
          
SyntaxError: unterminated string literal (detected at line 3)
def master_function(a, b, c, *args, d=100, e=-200, p, q, **kwargs):
    print("Positional arguments:")
    print("a:{}, b:{}, c:{}".format(a, b, c))
    print("Extra nonkeyword argument:")
    for i in range(len(args)):
        print("args[{}]:{}".format(i, args[i]))
    print("Default arguments:")
    print("d:{}, e:{}".format(d, e))
    print("Keyword only arguments:")
    print("p:{}, q:{}".format(p, q))
    print("Extra keyword:")
    for key in kwargs.keys():
        print("keyword:{}, value:{}".format(key, kwargs[key]))

        
master_function(10, 20, 30, 40, 50, 60, 70, e=-200, p=1.1, q=2.2, x=True, y=False)
Positional arguments:
a:10, b:20, c:30
Extra nonkeyword argument:
args[0]:40
args[1]:50
args[2]:60
args[3]:70
Default arguments:
d:100, e:-200
Keyword only arguments:
p:1.1, q:2.2
Extra keyword:
keyword:x, value:True
keyword:y, value:False
master_function(10, 20, 30, *(40, 50, 60, 70), e=-200, p=1.1, q=2.2, **{'x':True, 'y':False})
          
Positional arguments:
a:10, b:20, c:30
Extra nonkeyword argument:
args[0]:40
args[1]:50
args[2]:60
args[3]:70
Default arguments:
d:100, e:-200
Keyword only arguments:
p:1.1, q:2.2
Extra keyword:
keyword:x, value:True
keyword:y, value:False
T= (40, 50, 60, 70)
D = {'x':True, 'y':False}
master_function(10, 20, 30, *T, e=-200, p=1.1, q=2.2, **D)
Positional arguments:
a:10, b:20, c:30
Extra nonkeyword argument:
args[0]:40
args[1]:50
args[2]:60
args[3]:70
Default arguments:
d:100, e:-200
Keyword only arguments:
p:1.1, q:2.2
Extra keyword:
keyword:x, value:True
keyword:y, value:False
