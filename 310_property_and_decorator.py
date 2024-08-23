class Test: 
    def __init__(self, some_data): 
        self.n = some_data 

    def getter_of_n(self): 
        # getter logic 

    def setter_of_n(self, rhs): 
        # setter logic 

    def deleter_of_n(self): 
        # deleter logic 

    n = property(getter_of_n, setter_of_n, deleter_of_n) 

# == (ABOVE CODE IS EQUAL TO CODE BELOW )

class Test: 

    def __init__(self, some_Data): 
        self.n = some_Data 

    @property 
    def n(self): 
        # getter logic 

    @n.setter 
    def n(self, rhs): 
        # setter loic 

    @n.deleter 
    def n(self): 
        deleter logic 