class Test: 
    def non_static_method(X, Y): 
        print("type(X):", type(X))
        print("type(Y):", type(Y))

    @staticmethod 
    def f(X, Y): 
        print("type(X):", type(X))
        print("type(Y):", type(Y))


def main(): 
    t = Test() 
    t.non_static_method(100)
    t.f(100, 200)
    Test.f(1000, 2000)

main()