class Callable:
    def __init__(self, func_object):
        self.function_object = func_object

    def __call__(self, *args, **kwargs):
        return self.function_object(*args, **kwargs)


def combo_3(a, b, c, *args, d=100, e=200, p, q, **kwargs):
    print('In combo_3') 
    print(a, b, c) # pos 
    print(args) # extra nonkeyword 
    print(d, e)# default 
    print(p, q)# keyword only 
    print(kwargs) # extra keyword


C = Callable(combo_3)

C(10, 20, 30, 40, 50 ,60, 70, e=-200, p=1.1, q=2.2, x=True, y=False)
