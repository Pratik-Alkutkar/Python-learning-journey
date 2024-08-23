Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from functools import reduce
reduce(lambda x, y : x + y, map(lambda x : x ** 2 + 1, filter(lambda x : x % 2 == 1, range(1, 21)))) * reduce(lambda x, y : x * y, map(lambda x : x ** 3 + 1, filter(lambda x : x % 4 == 2, range(1, 51))))
412154983334109688867139737783887324563080621344169500
rs1 = 0
for i in range(1, 21):
    if i % 2 == 1:
        rs1 = rs1 + (i**2 + 1)

        
rs2 = 1
for i in range(1, 51):
    if i % 4 == 2:
        rs2 = rs2 * (i**3 + 1)

        
rs1 * rs2
412154983334109688867139737783887324563080621344169500
# Arithmetic Mean
(lambda I : reduce(lambda x, y : x+y)/len(I))([1,2,3,4,5])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    (lambda I : reduce(lambda x, y : x+y)/len(I))([1,2,3,4,5])
  File "<pyshell#14>", line 1, in <lambda>
    (lambda I : reduce(lambda x, y : x+y)/len(I))([1,2,3,4,5])
TypeError: reduce expected at least 2 arguments, got 1
(lambda I : reduce(lambda x, y : x+y, I)/len(I))([1,2,3,4,5])
3.0
(1+2+3+4+5)/5
3.0
arithmetic_mean = (lambda I : reduce(lambda x, y : x+y, I)/len(I))
rms = lambda I : (reduce(lambda x, y : x + y, map(lambda x : x ** 2, I)) / len(I))**0.5
rms([1,2,3,4,5])
3.3166247903554
((1**2+2**2+3**2+4**2+5**2)/5)**0.5
3.3166247903554
