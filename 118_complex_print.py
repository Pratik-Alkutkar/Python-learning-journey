class my_complex: 
    def __init__(self, init_x, init_y): 
        self.x = init_x 
        self.y = init_y 

    def __add__(self, other): 
        x_sum = self.x + other.x 
        y_sum = self.y + other.y 
        sum_object = my_complex(x_sum, y_sum)
        return sum_object 
    
    def show(self): 
        print("(", self.x, ")+i()", self.y, ")")

c1 = my_complex(1.1, 2.2)
c2 = my_complex(3.3, 4.4)
c3 = c1 + c2 

#print(c1)

c1.show() 


