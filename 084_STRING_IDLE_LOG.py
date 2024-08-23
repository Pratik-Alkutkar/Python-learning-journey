Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C = '''string data type'''
C = '''1: Ways of creation'''
s1 = 'Hello' # single quoted string
s
s2 = "Hello" # Double quoted string
s3 = 'Hello"World' # single quoted string containing double quoted string
s4 = "Hello'World"# double quoted string containing single quoted string
C = 'single quoted string containing double quote character (not double quoted string as written above)'
C = 'double quoted string containing single quote character (not single quoted string as written above)'
s5 = 'Hello\'World' # single quoted string containing single quote character using \
s6 = "Hello\"World" # double quoted string containing double quote character using \
print(s1)
Hello
print(s2)
Hello
print(s3)
Hello"World
print(s4)
Hello'World
print(s5)
Hello'World
print(s6)
Hello"World
s7 = "Hello\nWorld"  # double quote supports escape sequence
print(s7)
Hello
World
s8 = 'Hello\nWorld' # single quote also supports escape sequence
print(s8)
Hello
World
s9 = r'Hello\nWorld' # r prefix disable escape sequence . r = raw
print(s9)
Hello\nWorld
s10 = '''Hello World''' # triple quote using single '
s11 = """Hello,World""" # triple quote using double "
print(s10)
Hello World
print(s11)
Hello,World
s12 = """Tripled quoted string containing double quote " and single quote ' together without requiring \\"""
print(s12)
Tripled quoted string containing double quote " and single quote ' together without requiring \
s13 = """Triple quoted string can span
over
any number of lines
        and will preserve the formatting
            - Yogeshwar"""
print(s13)
Triple quoted string can span
over
any number of lines
        and will preserve the formatting
            - Yogeshwar
# Triple quoted string as doc string
def my_func():
    '''Documentation of my_func
        can be written using any number of lines
    '''
    pass

help(my_func)
Help on function my_func in module __main__:

my_func()
    Documentation of my_func
    can be written using any number of lines

class Date:
    '''Implementation of class Date
        Give info of all methods
    '''
    pass

help(Date)
Help on class Date in module __main__:

class Date(builtins.object)
 |  Implementation of class Date
 |  Give info of all methods
 |  
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

C = '''Built in functions string is compatible with'''
s = "Hello"
print(s)
Hello
type(s)
<class 'str'>
id(s)
1689258148592
len(s)
5
C = '''Built in operators on str'''
# concat
s1 = "Hello"
s2 = "World"
s3 = s1 + s2
print(s1)
Hello
print(s2)
World
print(s3)
HelloWorld
id(s1)
1689258148592
id(s2)
1689258214832
id(s3)
1689228012912
# Multiplication by scalar
s = "Hello"
s1 = s * 5
print(s)
Hello
print(s1)
HelloHelloHelloHelloHello
id(s)
1689258148592
id(s1)
1689258142704
s2 = s * 7
print(s)
Hello
print(s7)
Hello
World
print(s2)
HelloHelloHelloHelloHelloHelloHello
dashed_line = '-' * 80
print(dashed_line)
--------------------------------------------------------------------------------
# Index
s = "Hello,World"
s[0]
'H'
s[1]
'e'
s[2]
'l'
s1 = s[1]
s
'Hello,World'
s1
'e'
for i in range(len(s)):
    print(i, s[i])

    
0 H
1 e
2 l
3 l
4 o
5 ,
6 W
7 o
8 r
9 l
10 d
# range
s1 = s[:5]
print(s)
Hello,World
print(s1)
Hello
s
'Hello,World'
s2 = s[6:]
print(s)
Hello,World
print(s2)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    rint(s2)
NameError: name 'rint' is not defined. Did you mean: 'print'?
print(s2)
World
s3 = s[-5:]
print(s)
Hello,World
print(s3)
World
# slice operation, positive indices
s = "Hello,World!"
s1 = s[2 : 7 : 2]
print(s)
Hello,World!
print(s1)
loW
s2 = s[8 : 1 : -2]
print(s2)
rWol
s3 = [ 7 : 2 : -2]
SyntaxError: invalid syntax
s3 = s[7:2:-2]
print(s3)
o,l
s3 = s[7 : 2 : 2]
s4 = s[2 : 8 : -2]
print(s3)

print(s4)

# slice operation, negative indices
s5 = s[-8:-1:2]
print(s5)
oWrd
s5 = s[-2 : -8 : -2]
print(s5)
drW
s6 = s[-8 : -1 : -2]
s7 = s[-2:-8:2]
print(s6)

print(s7)

# slice operation, anchor charactes
s1 = s[:5:2]
s2 = s[:5:-2]
print(s1)
Hlo
p
print(s2)
!lo
s1 = s[1::2]
s2 = s[5::-2]
print(s1)
el,ol!
print(s2)
,le
s1 = s[::2]
print(s1)
HloWrd
s2 = s[::-1]
print(s2)
!dlroW,olleH
# membership testing operator
s = "aaBBBaaCCCaa"
'aa' in s
True
'xyz
SyntaxError: unterminated string literal (detected at line 1)

'xyz' in s
False
'a' in s
True
'B' in s
True
'C' in s
True
# String methods
s1 = "Hello,World\n"
s2 = "\n\tHelloWorld\n\n"
s3 = "\n\tHello"
print(s1)
Hello,World

print(s2)

	HelloWorld


print(s3)

	Hello
sr1 = s1.strip()
s1
'Hello,World\n'
sr1
'Hello,World'
sr2 = s2.strip()
s2
'\n\tHelloWorld\n\n'
print(sr2)
HelloWorld
sr3 = s3.strip()
print(s3)

	Hello
s3
'\n\tHello'
sr3
'Hello'
s4 = s2.rstrip()
s2
'\n\tHelloWorld\n\n'
s4
'\n\tHelloWorld'
s5 = s2.lstrip()
s2
'\n\tHelloWorld\n\n'
s5
'HelloWorld\n\n'
s2.strip()
'HelloWorld'
