Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import math
math.sin(math.pi)
1.2246467991473532e-16

================================ RESTART: Shell ================================
math
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    math
NameError: name 'math' is not defined
import math as m
math
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    math
NameError: name 'math' is not defined
m.sin(m.pi)
1.2246467991473532e-16
m.cos
<built-in function cos>
m.floor
<built-in function floor>
m.log2
<built-in function log2>

================================ RESTART: Shell ================================
from math import
SyntaxError: invalid syntax
from math import sin
math
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    math
NameError: name 'math' is not defined
sin(3.1415)
9.265358966049026e-05
cos
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    cos
NameError: name 'cos' is not defined
log2
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    log2
NameError: name 'log2' is not defined
math.sin
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    math.sin
NameError: name 'math' is not defined

================================ RESTART: Shell ================================
from math import sin as s
s(3.14)
0.0015926529164868282

================================ RESTART: Shell ================================
import math
m = math
del
SyntaxError: invalid syntax
del math
math
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    math
NameError: name 'math' is not defined
m.sin
<built-in function sin>
m.cos
<built-in function cos>
m.log2
<built-in function log2>
m.floor
<built-in function floor>

========================================================== RESTART: Shell =========================================================
import math
sin = math.sin
del math
sin(3.1415)
9.265358966049026e-05
cos
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    cos
NameError: name 'cos' is not defined
math
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    math
NameError: name 'math' is not defined
math.sin
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    math.sin
NameError: name 'math' is not defined
math.cos
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    math.cos
NameError: name 'math' is not defined
math.log2
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    math.log2
NameError: name 'math' is not defined

========================================================== RESTART: Shell =========================================================
import math
s = math.sin
del math
s(3.1415)
9.265358966049026e-05
sin
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    sin
NameError: name 'sin' is not defined. Did you mean: 'bin'?
math.sin
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    math.sin
NameError: name 'math' is not defined
math
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    math
NameError: name 'math' is not defined
