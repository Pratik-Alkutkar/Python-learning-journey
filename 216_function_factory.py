def PowerFunctionFactory(N): 
    def InnerFunction(x): 
        return x ** N
    return InnerFunction 

SquareFunction = PowerFunctionFactory(2)
result = SquareFunction(5)
print("result:", result)
result = SquareFunction(7)
print("result:", result)

CubeFunction = PowerFunctionFactory(3)
result = CubeFunction(5)
print(result)
result = CubeFunction(7)
print(result)



"""
GENERALISED DESCRIPTION OF FACTORY FUNCTION 
def factory_function(fp1, ...., fpk): 
    def inner_func(v1, .. , vn): 
        # definition of inner function 
        # which uses v1 to vn AND 
        # fp1 to fpk on RHS 
    return inner_func

"""
