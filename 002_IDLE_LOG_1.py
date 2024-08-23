Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sys
n = 2950189432
print(n)
2950189432
type(n)
<class 'int'>
id(n)
1950673594480
sys.getrefcount(n)
2
m = n
print(m)
2950189432
type(m)
<class 'int'>
id(m)
1950673594480
sys.getrefcount(m)
3