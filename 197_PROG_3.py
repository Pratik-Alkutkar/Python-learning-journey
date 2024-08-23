def f():
    def g1():
        print("In g1")
        print("leaving g1")
        def g2():
            print("in g2()")
            print("leaving g2()")
        print('random')
        g2()
        print('leaving g1')
    def h1():
        print("in f")
        def h2():
            print("in h2")
            def h3():
                print("in h3")
                print('leaving h3')
            print('ABCD')
            h3()
            print('PQRST')
        print('xyz')
        h2()
        print('abc')
    print('in f')
    h1()
    print('in f')
    g1()
n = 100
f()
print(n) 
