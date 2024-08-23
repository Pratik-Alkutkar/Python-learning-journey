Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s1="Hello"
s2="World"
s1 + s2
'HelloWorld'
L = [10, 20, 30]
L.append(40)
s1.
SyntaxError: invalid syntax
s1.__add__(s2)
'HelloWorld'
s1
'Hello'
s2
'World'
s1.__add__(s2)
'HelloWorld'
s1 + s2 # Python internally: s1.__add__(s2) # str.__add__(s1, s2)
'HelloWorld'
s1 + s2
'HelloWorld'
s1.__add__(s2)
'HelloWorld'
str.__add__(s1, s2)
'HelloWorld'
L
[10, 20, 30, 40]
L.append(59)
L
[10, 20, 30, 40, 59]
list.append(L, 60)
L
[10, 20, 30, 40, 59, 60]
for x in L::
    
SyntaxError: invalid syntax
for x in L:print(x)

10
20
30
40
59
60
L
[10, 20, 30, 40, 59, 60]
print(L)
[10, 20, 30, 40, 59, 60]
L + [-10, -20, -30]
[10, 20, 30, 40, 59, 60, -10, -20, -30]
L.append(600)
for x in L:
    print(x)

    
10
20
30
40
59
60
600
list.__str__(L)
'[10, 20, 30, 40, 59, 60, 600]'
list.__add__(L, [-10, -20, 30])
[10, 20, 30, 40, 59, 60, 600, -10, -20, 30]
list.append(L, 600)

L
[10, 20, 30, 40, 59, 60, 600, 600]
I = list.__iter__(L)
while True:
    try:
        n  = list.__next__(I)
        print(n)
    except StopIteration:
        break

    
Traceback (most recent call last):
  File "<pyshell#42>", line 3, in <module>
    n  = list.__next__(I)
AttributeError: type object 'list' has no attribute '__next__'. Did you mean: '__ne__'?
while True:
    try:
        n  = type(I).__next__(I)
        print(n)
    except StopIteration:
        break

    
10
20
30
40
59
60
600
600
I = list.__iter__(L)
while True:
    try:
        n  = type(I).__next__(I)
        print(n)
    except StopIteration:
        break

    
10
20
30
40
59
60
600
600
for x in L:
    print(x)

    
10
20
30
40
59
60
600
600
