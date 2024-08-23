class Date: 
    def __init__(self, dd, mm, yy): 
        self.day, self.month, self.year = dd, mm, yy 
    def __str__(self): 
        return "{}-{}-{}".format(self.day, self.month, self.year) 

d = Date(2, 2, 1971)
print(d)

with Date(1, 1, 1970) as d: 
    print(d)

