class Quadrilateral: 
    def __init__(self, init_s1:float, init_s2:float, init_s3:float, init_s4:float): 
        self.s1 = init_s1 
        self.s2 = init_s2 
        self.s3 = init_s3 
        self.s4 = init_s4 
    
    def perimeter(self): 
        return self.s1 + self.s2 + self.s3 + self.s4 
    
    def area(self): 
        s = self.perimeter() / 2 
        return ((s-self.s1) * (s-self.s2) * (s-self.s3) * (s-self.s4)) ** 0.5
    
class Rectangle(Quadrilateral): 
    def __init__(self, length:float, breadth:float): 
        Quadrilateral.__init__(self, length, breadth, length, breadth)
        self.L = length 
        self.B = breadth 

    def area(self): 
        return self.L * self.B 
    
    def get_diagonal_length(self): 
        return (self.B**2 + self.L**2) ** 0.5 
    
class Square(Rectangle): 
    def __init__(self, init_s): 
        Rectangle.__init__(self, init_s, init_s) 
        self.s = init_s 
        # s1, s2, s3, s4, B, L, init_s 

    def area(self): 
        return self.s ** 2 
    
    def get_diagonal_length(self):
        return self.s * (2 ** 0.5)
            
def main(): 
    Q = Quadrilateral(1.2, 2.6, 3.1, 2.8) 
    periQ = Q.perimeter()
    areaQ = Q.area() 

    R = Rectangle(10.0, 5.0)
    periR = R.perimeter() # Will be resolved from Quadrilateral.perimeter() 
    areaR = R.area() # Will be resolved from Reactangle.area() 
    diagR = R.get_diagonal_length() # will be resolved from Rectangle.get_diagonal_length() 

    S = Square(7.0)
    periS = S.perimeter() # From Quadrilateral 
    areaS = S.area() # from Square 
    diagS = S.get_diagonal_length() # from Square 

main()