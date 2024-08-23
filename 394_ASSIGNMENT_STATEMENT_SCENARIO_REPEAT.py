Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n = 10
type(n)
<class 'int'>
id(n)
2818145911312
print(n)
10
import sys
sys.getrefcount(n)
63
# 1
n = 10
print(n)
10
t
type(n)
<class 'int'>
id(n)
2818145911312
sys.getrefcoount(n)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ys.getrefcoount(n)
NameError: name 'ys' is not defined. Did you mean: 'sys'?
sys.getrefcount(n)
63
# 2
n = 10
print(n)
10
type(n)
<class 'int'>
id(n)
2818145911312
sys.getrefcount(n)
63
# 3
n = 10
print(n)
10
type(n)
<class 'int'>
id(n)
2818145911312
sys.getrefcount(n)
63
# 4
n = 10
print(n)
10
type(n)
<class 'int'>
id(n)
2818145911312
sys.getrefcount(n)
63
# 5
n = 10
print(n)
10
type(n)
<class 'int'>
id(n)
2818145911312
sys.getrefcount(n)
63
# assignment statement scenario #2
p = 100
id(p)
2818145914192
sys.getrefcount(p)
22
q = p
id(q)
2818145914192
sys.getrefcount(p)
23
# 1
m = 200
id(m)
2818145917392
sys.getrefcount(m)
8
k = m
id(k)
2818145917392
sys.getrefcount(k)
9
# 3
u = 300
id(u)
2818181755344
sys.getrefcount(u)
2
v = u
id(v)
2818181755344
sys.getrefcount(v)
3
# 4
a = -1024
id(a)
2818181756368
b = a
id(b)
2818181756368
sys.getrefcoount(b)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    sys.getrefcoount(b)
AttributeError: module 'sys' has no attribute 'getrefcoount'. Did you mean: 'getrefcount'?
sys.getrefcount(a)
3
# 5
i = 4000
id(i)
2818181754928
j = i
id(j)
2818181754928
i = 5000
id(i)
2818181753040
sys.getrefcount(i)
2
j = i
id(j)
2818181753040
sys.getrefcount(i)
3
# assignment statement : scenario 3
n = 100
id(n)
2818145914192
sys.getrefcount(n)
24
n = 200
id(n)
2818145917392
sys.geterefcount(100)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    sys.geterefcount(100)
AttributeError: module 'sys' has no attribute 'geterefcount'. Did you mean: 'getrefcount'?
sys.getrefcount(100)
25
a = 100
id(a)
2818145914192
sys.getrefcount(a)
25
b = a
sys.getrefcount(b)
26
id(b)
2818145914192
b = 300
id(b)
2818181753424
sys.getrefcount(a)
25
# 1
a = 10000
id(a)
2818181753456
sys.getrefcount(a)
2
b = a
id(b)
2818181753456
sys.getrefcount(a)
3
b = 20000
id(b)
2818181756368
sys.getrefcount(a)
2
# 2
a = 3.14
id(a)
2818181749776
sys.getrefcount(a)
2
b = a
id(b)
2818181749776
sys.getrefcount(a)
3
b = 6.28
id(b)
2818181753456
sys.getrefcount(a)
2
# 3
a = "Hello"
id(a)
2818183292720
sys.getrefcount(a)
2
b = a
id(b)
2818183292720
sys.getrefcount(a)
3
b = "World"
id(b)
2818183294320
sys.getrefcount(a)
2
# 4
a = [100, 200, 300, 400]
id(a)
2818183280128
sys.getrefcount(a)
2
b = a
id(b)
2818183280128
sys.getrefcount(a)
3
b = (1, 2, 3)
id(b)
2818183334336
sys.getrefcount(a)
2
# 5
a = {100, 200, 300}
id(a)
2818182828480
sys.getrefcount(a)
2
b  = a
id(b)
2818182828480
b = {'a':10, 'b':20}
id(b)
2818183361728
sys.getrefcount(a)
2
