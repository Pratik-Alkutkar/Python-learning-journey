class Quadrilateral: 
    def __init__(self, init_s1:float, init_s2:float, init_s3:float, init_s4:float): 
        if type(init_s1) != int and type(init_s1) != float: 
            raise TypeError("Bad Type for side of the square")
        if type(init_s2) != int and type(init_s2) != float: 
            raise TypeError("Bad Type for side of the square")
        if type(init_s3) != int and type(init_s3) != float: 
            raise TypeError("Bad Type for side of the square")
        if type(init_s4) != int and type(init_s4) != float: 
            raise TypeError("Bad Type for side of the square")
        if init_s1 <= 0 or init_s2 <= 0 or init_s3 <= 0 or init_s4 <= 0: 
            raise ValueError("Side of quadrilateral cannot be negative")
        if (    
                (init_s1 > init_s2 + init_s3 + init_s4) or 
                (init_s2 > init_s1 + init_s3 + init_s4) or 
                (init_s3 > init_s1 + init_s2 + init_s4) or 
                (init_s4 > init_s1 + init_s2 + init_s3)
        ):
            raise ValueError("Summation of three sides of quadrilateral must be greater than the fourth")

        self.s1 = init_s1 
        self.s2 = init_s2 
        self.s3 = init_s3 
        self.s4 = init_s4 
    
    def perimeter(self): 
        return (self.s1 + self.s2 + self.s3 + self.s4)
    
    def area(self): 
        # s = self.perimeter() / 2 
        s = (self.s1 + self.s2 + self.s3 + self.s4)/2 
        return ((s - self.s1) * (s - self.s2) * (s - self.s3) * (s - self.s4))**0.5

class Square(Quadrilateral): 
    def __init__(self, init_s:float): 
        if type(init_s) != int and type(init_s) != float: 
            raise TypeError("Bad type for square")
        if init_s <= 0: 
            raise ValueError("Side of square must be positive")
        Quadrilateral.__init__(self, init_s, init_s, init_s, init_s)
        self.s = init_s 

    def get_diagonal_length(self): 
        return self.s * (2 ** 0.5)
               
def main(): 
    Q1 = Quadrilateral(1.5, 4.5, 3.8, 2.9)
    P = Q1.perimeter() 
    A = Q1.area() 
    print("Perimeter(Q1)=%.3f Area(Q1)=%.3f" % (P, A))
    S = Square(10.5)
    P_sq = S.perimeter()    # Quadrilateal.perimeter(S)
    A_sq = S.area()         # Quadrilateral.area(S)
    print("Perimeter(Square)=%.3f Area(Square)=%.3f" % (P_sq, A_sq))
    Diag_Len = S.get_diagonal_length()
    print("Diag_Len = %.3f" % Diag_Len)

main()