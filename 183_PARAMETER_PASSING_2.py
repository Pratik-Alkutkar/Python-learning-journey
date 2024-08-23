Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Paramter passing part 2
# 6. Extra-keyword argument

def test(**kwargs):
    for key in kwargs.keys():
        print(key, kwargs[key])

        
test(a=10, b=20, c=30)
a 10
b 20
c 30
test(text='Exit', command=exit, fg='green', bg='red')
text Exit
command Use exit() or Ctrl-D (end-of-file) to exit
fg green
bg red
exit
Use exit() or Ctrl-D (end-of-file) to exit
test(p=1.1, q=2.2, r=3.3)
p 1.1
q 2.2
r 3.3
test(**{'a':10, 'b':20, 'c':30})
a 10
b 20
c 30
D = {'a':10, 'b':20, 'c':30, 'd':40}
test(**D)
a 10
b 20
c 30
d 40
def test_1(*args):
    print(args)

    
test_1(10, 20, 30, 40, 50)
(10, 20, 30, 40, 50)
test_1(*(10, 20, 30, 40, 50))
(10, 20, 30, 40, 50)
T = (10, 20, 30)
test_1(*T)
(10, 20, 30)
# 7 Default parameter
def test(a=10, b=20, c=30):
    print("a:", a)
    print("b:", b)
    print("c:", c)

    
test()
a: 10
b: 20
c: 30
test(100)
a: 100
b: 20
c: 30
test(100, 200, 300)
a: 100
b: 200
c: 300
test(a=100)
a: 100
b: 20
c: 30
test(b=200)
a: 10
b: 200
c: 30
test(c=300)
a: 10
b: 20
c: 300
def test(drink): print(drink)

test('tea')
tea
def test(drink='tea'):print(drink)

test()
tea
test(drink='coffee')
coffee
def test(a=10, b=20, c=30):
    print("a:", a)
    print("b:", b)
    print("c:", c)

    
test(100)
a: 100
b: 20
c: 30
test(10, b=200, c=30)
a: 10
b: 200
c: 30
test(10, 20, 300)
a: 10
b: 20
c: 300
# Keyword only arguments
def test(*args, p, q):
    print(args, type(args))
    print(p, type(p))
    print(q, type(q))

    
test(10, 20, 30, 40, 50, 60, p=1.1, q=2.2)
(10, 20, 30, 40, 50, 60) <class 'tuple'>
1.1 <class 'float'>
2.2 <class 'float'>
test(10, 20, 30, 40, 50, 60)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    test(10, 20, 30, 40, 50, 60)
TypeError: test() missing 2 required keyword-only arguments: 'p' and 'q'
def test(a, b, c, *args, p, q):
    print(a, b, c)
    print(args)
    print(p, q)

    
test(100, 200, 300, 400, 500, 600, 700, p=1.1, q=2.2)
100 200 300
(400, 500, 600, 700)
1.1 2.2
