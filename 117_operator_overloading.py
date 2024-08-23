class my_complex: 
    def __init__(self, r1:float, r2:float): 
        self.x = r1 
        self.y = r2 

    def __add__(self, other): 
        print("Control flow was here")
        sum_x = self.x + other.x 
        sum_y = self.y + other.y 
        c_sum = my_complex(sum_x, sum_y)
        return c_sum 

c1 = my_complex(1.1, -2.3)
c2 = my_complex(-6.5, 1.3)

print("type(c1):", type(c1))
print("type(c2):", type(c2))

#c3 = c1.summation(c2) # my_complex.summation(c1, c2)

print("start")
c3 = c1 + c2 # my_complex.__add__(c1, c2)
print("end")
