"""
@Author: Pratik Pramod Alkutkar
@Goal: Write a class Test with its object 't' having 
       attribute named 'n'. 
       Make 'n' a managed attribute using a property method. 
       Strategy for attribute management: 
       1) rhs strategy: t.n on rhs should return square of 
       integer value associated with 'n' 
       2) lhs strategy : default behaviour 
       3) del strategy: Don't allow removal of 'n' from 't'. 
        raise AttributeError exception if the attempt is made. 
"""

import sys 

class Test: 
    def __init__(self, init_n): 
        if type(init_n) != int: 
            raise TypeError("Initializer of 'n' must be an int")
        self.n = init_n 

    def get_method(self): 
        return self.__dict__['n'] ** 2 
    
    def set_method(self, rhs_object): 
        self.__dict__['n'] = rhs_object 

    def del_method(self): 
        raise AttributeError("Cannot remove 'n' from object")
    
    n = property(get_method, set_method, del_method) 

def main(): 
    t = Test(7) 
    print("t.n:{}".format(t.n))
    t.n = 11 
    print("t.n:{}".format(t.n))
    try: 
        del t.n
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data)
    sys.exit(0) 

main()

