Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sys
m = 2957381043
sys.getrefcount(m)
2
help(sys.getrefcount)
Help on built-in function getrefcount in module sys:

getrefcount(object, /)
    Return the reference count of object.
    
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to
    getrefcount().

n = m
sys.getrefcount(m)
3
sys.getrefcount(n)
3
id(m)
2448094980144
id(n)
2448094980144
n = 92510423
sys.getrefcount(n)
2
sys.getrefcount(m)
2

================================ RESTART: Shell ================================
