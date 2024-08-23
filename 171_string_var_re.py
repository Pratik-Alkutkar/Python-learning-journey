class StringVar: 
    def __init__(self, init_s=""): 
        if type(init_s) != str: 
            raise TypeError 
        self.s = init_s 

    def get(self): 
        return self.s 
    
    def set(self, new_val:str): 
        if type(new_val) != str: 
            raise TypeError 
        self.s = new_val