"""
@goal: To describe a pattern for attribute management using descriptor protocol
attribute named 'attr' of class C must be managed. 
"""

class Descriptor_of_attr: 
    def __get__(self, obj, cls): 
        """
        Replace pass by getter logic 
        """
        pass 

    def __set__(self, obj, rhs): 
        """
        Replace pass by setter logic
        """
        pass 

    def __delete__(self, obj): 
        """
        Replace pass by deleter logic
        """
        pass 
    

class C: 
    def __init__(self, some_data): 
        self.attr = some_data 

    attr = Descriptor_of_attr() 

def main(): 
    objC = C(data)
    lhs = objC.attr # Descriptor_of_attr.__get__(attr, objC, C)
    objC.attr = rhs # Descriptor_of_attr.__set__(attr, objC, rhs)
    del objC.attr # Descriptor_of_attr.__delete__(attr, objC)

main()
    