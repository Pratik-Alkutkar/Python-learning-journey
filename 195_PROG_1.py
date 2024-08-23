# Program #1

print("global:start of program")
def f():
    print("f:Entered f()")
    def g():
        print("g:Entered g()")
        print("g:Entered g()")
    print("f:Defined g()")
    g()
    print("f:Returned from g()")
    g()
    print("f:Leaving f()")
print("global:defined f()")
f()
print("global:end of program")

"""
global:start of program
global:defined f()
f:Entered f()
f:Defined g()
g:Entered g()
g:Entered g()
f:Returned from g()
g:Entered g()
g:Entered g()
f:Leaving f()
global:end of program
"""
