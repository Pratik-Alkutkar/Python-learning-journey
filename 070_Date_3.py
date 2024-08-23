import sys 

class Date: 
    def __init__(self, init_day:int, init_month:int, init_year:int): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year 

    def show(self): 
        print("%d-%d-%d" % (self.day, self.month, self.year))

    def set_day(self, new_day:int): 
        self.day = new_day 

    def set_month(self, new_month:int): 
        self.month = new_month 

    def set_year(self, new_year:int): 
        self.year = new_year 

def main(): 
    D = Date(20, 1, 2023)
    D.show() 
    D.set_day(31)
    D.set_month(12)
    D.set_year(2022)
    D.show() 

main()