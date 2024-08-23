class my_decorator: 
    def __init__(self, F): 
        self.F = F 

    def __call__(self, *args, **kwargs): 
        print("PREPROCESSING")
        ret = self.F(*args, **kwargs)
        print("POSTPROCESSING")
        return ret 

@my_decorator
def my_function(a, b): 
    rs1 = a + b 
    rs2 = a - b 
    rs = rs1 * rs2 
    return rs 

ret = my_function(100, 200)
print("ret:", ret)

ret = my_function(200, 300)
print("ret:", ret)