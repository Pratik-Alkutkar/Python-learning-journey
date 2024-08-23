Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n1 = 10
print(n1)
10
n1
10
class CPA_int:
    def __init__(self, init_n):
        self.n = init_n
    def __str__(self):
        return str(self.n)

    
n = CPA_int(150)
print(n)
150
n
<__main__.CPA_int object at 0x000002DB8E009D20>
n
<__main__.CPA_int object at 0x000002DB8E009D20>
class CPA_int:
    def __init__(self, init_n):
        self.n = init_n
    def __str__(self):
        return str(self.n)
    def __repr__(self):
        return str(self.n)

    
n = CPA_int(150)
print(n)
150
n
150
class CPA_int:
    def __init__(self, init_n):
        self.n = init_n
    def __str__(self):
        print("Support for print(n) where n is CPA_int object")
        return str(self.n)
    def __repr__(self):
        print("Support for >>>n where n is CPA_int object")
        return str(self.n)

    
n = CPA_int(150)
print(n)
Support for print(n) where n is CPA_int object
150
n
Support for >>>n where n is CPA_int object
150
class CPA_int:
    def __init__(self, init_n):
        self.n = init_n
    def __str__(self):
        return str(self.n)
    __repr__ = __str__

    
n = CPA_int(550)
print(n)
550
n
550
s = "Hello\nWorld"
s1 = r"Hello\nWorld"
print(s)
Hello
World
print(s1)
Hello\nWorld
print(s)
Hello
World
s
'Hello\nWorld'
f = 3.14
print(f)
3.14
f
3.14
