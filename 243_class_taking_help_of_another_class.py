class C1:
    def __init__(self, some_data):
        # write a constructor

    def f(self):
        # LOGIC 

class C2:
    def __init__(self):
        self.objC1 = C1(init_data)

    def f(self):
        return self.objC1.f()

# COMPOSITION
# AGGREGATION

# has-a
# is-a



objC

objC2 = C2()
objC2.f()

class T_iterator:
    def __init__(self, G):
        self.G = G

    def __next__(self):
        return self.G.__next__()


class T:

    def __iter__(self):
        def get_generator():
            yield rhs

        G = get_generator()
        
        return T_iterator(G)

objT = T()

for x in objT:
    print(x)


I = objT.__iter__() # T_iterator

while True:
    try:
        n = I.__next__()
        print(n)
    except StopIteration:
        break 