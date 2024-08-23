def my_decorator(cls): 
    print("cls.__name__:", cls.__name__)
    return cls 

@my_decorator 
class Test: 
    pass 

class Student: 
    pass 

@my_decorator
class Date: 
    pass 