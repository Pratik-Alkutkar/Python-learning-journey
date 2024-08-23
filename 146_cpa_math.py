print("__name__:", __name__)

def cpa_fact(n:int)->int: 
    if type(n) != int: 
        raise TypeError("Bad type:n")
    if n < 0: 
        raise ValueError("Factorial of negative number cannot be computed")
    if n == 0: 
        return (1)
    result = 1 
    k = 1
    while k <= n: 
        result = result * k 
        k = k + 1 
    return (result) 

def cpa_sin(x:float)->float: 
    if type(x) != int and type(x) != float: 
        raise TypeError("Bad type for angle")
    return (x - (x**3/cpa_fact(3)) + (x**5/cpa_fact(5)) - (x**7/cpa_fact(7)) + 
            (x**9/cpa_fact(9)) - (x**11/cpa_fact(11)))

def cpa_cos(x:float)->float: 
    if type(x) != int and type(x) != float: 
        raise TypeError("Bad type for angle")
    return (1 - (x**2/cpa_fact(2)) + (x**4/cpa_fact(4)) - (x**6/cpa_fact(6)) + 
            (x**8/cpa_fact(8)) - (x**10/cpa_fact(10)))

if __name__ == '__main__': 
    import math 
    N = 5 
    result_1 = math.factorial(N)
    result_2 = cpa_fact(N)
    print("result_1:%d, result_2:%d" % (result_1, result_2))

    angle = math.pi / 2 
    sin_angle_p = math.sin(angle)
    cos_angle_p = math.cos(angle)

    sin_angle = cpa_sin(angle)
    cos_angle = cpa_cos(angle)

    print("sin_angle_p:%.6f, sin_angle:%.6f" % (sin_angle_p, sin_angle))
    print("cos_angle_p:%.6f, cos_angle:%.6f" % (cos_angle_p, cos_angle))