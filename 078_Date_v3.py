class Date: 
    def __init__(self, init_day, init_month, init_year): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year 

    # day attribute getter 
    def get_day(self): 
        return self.day 

    # day attribute setter 
    def set_day(self, new_day): 
        self.day = new_day

    # month attribute getter 
    def get_month(self): 
        return self.month 

    # month attribute setter 
    def set_month(self, new_month): 
        self.month = new_month 

    # year attribute getter 
    def get_year(self): 
        return self.year 

    # year attribute setter 
    def set_year(self, new_year): 
        self.year = new_year 

def main(): 
    D = Date(31, 1, 2023)               # STEP IN 
    
    dd = D.get_day() # Date.get_day(D)  # STEP IN 
    print("dd=", dd)                    # STEP OVER 
    D.set_day(24) # Date.set_day(D, 24) # STEP IN 
    dd = D.get_day()                    # STEP IN 
    print("dd=", dd)                    # STEP OVER  

    mm = D.get_month()  # STEP IN
    print("mm=", mm)    # STEP OVER
    D.set_month(5)      # STEP IN
    mm = D.get_month()  # STEP IN
    print("mm=", mm)    # STEP OVER

    yy = D.get_year()   # STEP IN
    print("yy=", yy)    # STEP OVER
    D.set_year(2025)    # STEP IN
    yy = D.get_year()   # STEP IN
    print("yy=", yy)    # STEP OVER

main()                  # STEP IN 
