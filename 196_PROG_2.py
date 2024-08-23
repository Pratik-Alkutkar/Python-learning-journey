# Program 2

print("in global")
def f():
    print("In f")
    def g():
        print("In g")
        def h():
            print("In h")
            print("leaving h")
        print("done defining h")
        h()
        print("leaving g")
    g()
    print("leaving f")
N=100
f()
print("N = %d" % N) 

"""
in global
In f
In g
done defining h
In h
leaving h
leaving g
leaving f
N = 100
"""
