import sys 

class Descriptor_of_n: 
    def __get__(self, obj, cls): 
        return obj.__dict__['n'] ** 2  # return obj.n**2
    
    def __set__(self, obj, rhs): 
        obj.__dict__['n'] = rhs 

    def __delete__(self, obj): 
        raise AttributeError("Cannot remove 'n' from object")
    
class Test: 
    def __init__(self, init_n): 
        self.n = init_n 

    n = Descriptor_of_n()

def main(): 
    t = Test(7) 
    print("t.n:{}".format(t.n)) # t.n == Descriptor_of_n.__get__(n, t, Test)
    t.n = 11 # Descriptor_of_n.__set__(n, t, 11)
    print("t.n:{}".format(t.n))
    try: 
        del t.n # Descriptor_of_n.__delete__(n, t)
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data)
    sys.exit(0) 

main()