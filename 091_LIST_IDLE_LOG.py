Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
C = """List methods continued..."""
L = []
b = True
n = 10
f = 3.14
s = "Hello"
T= (10, 20, 30)
S = {-1, -2}
L
[]
L.append(b)
L
[True]
len(L)
1
L.append(n)
L
[True, 10]
len(L)
2
L.append(f)
L
[True, 10, 3.14]
len(L)
3
L.append(s)
L
[True, 10, 3.14, 'Hello']
len(L)
4
L
[True, 10, 3.14, 'Hello']
L.append(T)
L
[True, 10, 3.14, 'Hello', (10, 20, 30)]
len(L)
5
L.append(S)
L
[True, 10, 3.14, 'Hello', (10, 20, 30), {-1, -2}]
len(L)
6
# extend method
L = []
L.append(True)
L.append(10)
L
[True, 10]
T = (100, 200, 300)
L.extend(T)
L
[True, 10, 100, 200, 300]
len(L)
5
# insert method
L = [10, 20, 30, 40, 50, 60]
# insert = insert at given index
L.insert(0, -1)
L
[-1, 10, 20, 30, 40, 50, 60]
L.insert(3, -1)
L
[-1, 10, 20, -1, 30, 40, 50, 60]
L.insert(len(L),-1) # L.append(-1)
L
[-1, 10, 20, -1, 30, 40, 50, 60, -1]
# Insert at beg: L.insert(0, elem)
# Insert at end: L.insert(len(L), elem)
# Let d be a data element already present in list L
# Let 'element' be a data to be added in L
# How to put 'element' just before 'd' and how to put element
# just after 'd'
# Inserting element before d in L
# L.insert(L.index(d), element)
# L.insert(L.index(d) + 1, element)
L
[-1, 10, 20, -1, 30, 40, 50, 60, -1]
L.insert(L.index(40), -1)
L
[-1, 10, 20, -1, 30, -1, 40, 50, 60, -1]
L.insert(L.index(40) + 1, -1)
L
[-1, 10, 20, -1, 30, -1, 40, -1, 50, 60, -1]

=========== RESTART: C:/Users/yoges/OneDrive/Documents/CPA/PYTHON/BATCH_CODES/BATCH_46/SESSION_037/interview_exercise.py ==========
BEFORE: [10, 15, 25, 30, 40, 50]
AFTER: ['E', 10, 'O', 15, 'O', 25, 'E', 30, 'E', 40, 'E', 50]
C = """Removal methods"""
L = [10, 20, 30, 40, 50, 60, 80, 90, 100, 110, 120, 130]
# index, range, slice based removal using del statement
L[4]
50
del L[4]
L
[10, 20, 30, 40, 60, 80, 90, 100, 110, 120, 130]
# del L[i], del L[i:j], del L[i:j:k]
L[2:5]
[30, 40, 60]
del L[2:5]
L
[10, 20, 80, 90, 100, 110, 120, 130]
L[1:7:4]
[20, 110]
del L[1:7:4]
L
[10, 80, 90, 100, 120, 130]
# data based removal
L.remove(100)
L
[10, 80, 90, 120, 130]
L.remove(120)
# L.remove(120)     del L[L.index(120)]
L
[10, 80, 90, 130]
L.clear()
L
[]
L =[10, 20, 30, 40, 50, 60]
print(L)
[10, 20, 30, 40, 50, 60]
L = []
L
[]
L1 = [10, 20, 30, 40, 50, 60]
L2 = L1
id(L1)
2443476400896
id(L2)
2443476400896
L1
[10, 20, 30, 40, 50, 60]
L2
[10, 20, 30, 40, 50, 60]
L1 = []
L1
[]
id(L1)
2443476497024
L2
[10, 20, 30, 40, 50, 60]
id(L2)
2443476400896
M = [100, 200, 300]
N = M
id(M)
2443445222720
id(N)
2443445222720
M
[100, 200, 300]
N
[100, 200, 300]
M.clear()
M
[]
N
[]
id(M)
2443445222720
L = [10, 20, 30, 40, 50]
n = L.pop(0)
L
[20, 30, 40, 50]
n
10
L.pop()
50
L
[20, 30, 40]
L.pop()
40
L
[20, 30]
L.pop()
30
L.pop()
20
L
[]
L.pop()
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    L.pop()
IndexError: pop from empty list
del L[i]