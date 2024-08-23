# Program #1

print("global:start of program")
def f():
    print("f:Entered f()")
    def g():
        print("g:Entered g()")
        print("g:Leaving g()")
    print("f:Defined g()")
    g()
    print("f:Returned from g()")
    g()
    print("f:Leaving f()")
print("global:defined f()")
f()
print("global:end of program")

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
print("N=%d" % N)
