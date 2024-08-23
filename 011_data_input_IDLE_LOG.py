Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n = int(10)
print(n)
10
type(n)
<class 'int'>
id(n)
1553348821520
n = 100
m = int(100)
n = int(100)
print(n)
100
type(n)
<class 'int'>
s = "472
SyntaxError: unterminated string literal (detected at line 1)
s="472"
print(s)
472
type(s)
<class 'str'>
s/2
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    s/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
k = int(s)
print(k)
472
type(k)
<class 'int'>
print(s)
472
type(s)
<class 'str'>
id(s)
1553385832944
id(k)
1553384600080
