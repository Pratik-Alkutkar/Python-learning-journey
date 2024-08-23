Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C = """List methods continued..."""
L = [10, 20, 30, 40, 50, 60]
# Modification
# index assignment, range assignment, slice assignment
# Index assignment: L[i] = value
# Range assignment: L[i:j]= iterable
# Slice assignment: L[i:j:k] = iterable
print(L)
[10, 20, 30, 40, 50, 60]
L[1] = 200
print(L)
[10, 200, 30, 40, 50, 60]
L = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
L[3 : 8] = [400, 500, 600, 700, 800]
L
[10, 20, 30, 400, 500, 600, 700, 800, 90, 100, 110, 120]
L[1 : 4]
[20, 30, 400]
L[1:4] = [1, 2, 3, 4, 5]
L
[10, 1, 2, 3, 4, 5, 500, 600, 700, 800, 90, 100, 110, 120]
L[1:4]
[1, 2, 3]
L[1:4]=[500]
L
[10, 500, 4, 5, 500, 600, 700, 800, 90, 100, 110, 120]
L[3 : 6]
[5, 500, 600]
L[3:6] = []
L
[10, 500, 4, 700, 800, 90, 100, 110, 120]
L[1 : 8 : 2]
[500, 700, 90, 110]
L[1 : 8 : 2] = [-1, -2]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    L[1 : 8 : 2] = [-1, -2]
ValueError: attempt to assign sequence of size 2 to extended slice of size 4
L[1 : 8 : 2] = [-1, -2, -3, -4, -5]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    L[1 : 8 : 2] = [-1, -2, -3, -4, -5]
ValueError: attempt to assign sequence of size 5 to extended slice of size 4
L[1 : 8 : 2] = [-1, -2, -3, -4]
L
[10, -1, 4, -2, 800, -3, 100, -4, 120]
# reverse() = Mutable reversal
L
[10, -1, 4, -2, 800, -3, 100, -4, 120]
LR = L[::-1]
L
[10, -1, 4, -2, 800, -3, 100, -4, 120]
LR
[120, -4, 100, -3, 800, -2, 4, -1, 10]
id(L)
2277481306944
id(LR)
2277517552768
L = [10, 20, 30, 40]
L.reverse()
L
[40, 30, 20, 10]
# sort() = Mutable sorting
L = [1, 5, 6, 2, 3, 9]
LS = sorted(L)
id(L)
2277517871232
id(LS)
2277517548352
L
[1, 5, 6, 2, 3, 9]
LS
[1, 2, 3, 5, 6, 9]
L = [1, 2, "Hello", (10, 20, 30)]
sorted(L)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    sorted(L)
TypeError: '<' not supported between instances of 'str' and 'int'
L = [1, 5, 6, 2, 3, 9]
sorted(L)
[1, 2, 3, 5, 6, 9]
L
[1, 5, 6, 2, 3, 9]
L.sort()
L
[1, 2, 3, 5, 6, 9]
sorted(L, reverse=True)
[9, 6, 5, 3, 2, 1]
