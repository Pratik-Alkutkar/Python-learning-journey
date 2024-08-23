"""
class Date: 
    def __init__(self, init_day, init_month, init_year): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year 
    def get_day(self): 
        return self.day 
    def get_month(self): 
        return self.month 
    def get_year(self): 
        return self.year 
    def set_day(self, new_day): 
        self.day = new_day 
    def set_month(self, new_month): 
        self.month = new_month 
    def set_year(self, new_year): 
        self.year = new_year 
    def __str__(self): 
        return "{}-{}-{}".format(self.day, self.month, self.year)

D = Date(1, 1, 1970)
dd, mm, yy = D.get_day(), D.get_month(), D.get_year()
print(dd, mm, yy)
D.set_day(2)
D.set_month(2)
D.set_year(1975)
dd, mm, yy = D.get_day(), D.get_month(), D.get_year()
print(dd, mm, yy)
print(D)
"""

# MANUAL CREATION OF DATE 

cls_name = "Date"
cls_bases = (object, )
cls_dict = {}
cls_body = """
def __init__(self, init_day, init_month, init_year): 
    self.day = init_day 
    self.month = init_month 
    self.year = init_year 
def get_day(self): 
    return self.day 
def get_month(self): 
    return self.month 
def get_year(self): 
    return self.year 
def set_day(self, new_day): 
    self.day = new_day 
def set_month(self, new_month): 
    self.month = new_month 
def set_year(self, new_year): 
    self.year = new_year 
def __str__(self): 
    return "{}-{}-{}".format(self.day, self.month, self.year)
"""
exec(cls_body, globals(), cls_dict)

Date = type(cls_name, cls_bases, cls_dict)

D = Date(1, 1, 1970)
dd, mm, yy = D.get_day(), D.get_month(), D.get_year()
print(dd, mm, yy)
D.set_day(2)
D.set_month(2)
D.set_year(1975)
dd, mm, yy = D.get_day(), D.get_month(), D.get_year()
print(dd, mm, yy)
print(D)