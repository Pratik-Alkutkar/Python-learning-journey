Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
r1 = range(10, 20)
type(r1)
<class 'range'>
for x in r1:
    print(x)

    
10
11
12
13
14
15
16
17
18
19
r2 = range(10)
for x in r2:
    print(x)

    
0
1
2
3
4
5
6
7
8
9
L = [10, 20, 30, 40, 50, 60]
i = 0
while i < len(L):
    print(i, L[i])
    i = i + 1

    
0 10
1 20
2 30
3 40
4 50
5 60
for x in L:
    print(x)

    
10
20
30
40
50
60
R = range(6)
for i in R:
    print(i)

    
0
1
2
3
4
5
R = range(len(L))
for i in R:
    print(i, L[i])

    
0 10
1 20
2 30
3 40
4 50
5 60
for i in range(len(L)):
    print(i, L[i])

    
0 10
1 20
2 30
3 40
4 50
5 60
