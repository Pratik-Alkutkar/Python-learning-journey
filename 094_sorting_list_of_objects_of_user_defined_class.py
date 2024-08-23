class Employee: 
    def __init__(self, init_emp_id, init_emp_name, init_emp_city, init_emp_sal): 
        self.emp_id = init_emp_id 
        self.emp_name = init_emp_name 
        self.emp_city = init_emp_city 
        self.emp_sal = init_emp_sal 
        
    def __lt__(self, other): 
        return self.emp_id < other.emp_id 
    
    def __le__(self, other): 
        return self.emp_id <= other.emp_id 
    
    def __gt__(self, other): 
        return self.emp_id > other.emp_id 
    
    def __ge__(self, other): 
        return self.emp_id >= other.emp_id 
    
    def __eq__(self, other): 
        return self.emp_id == other.emp_id 
    
    def __ne__(self, other): 
        return self.emp_id != other.emp_id 
    
    def __str__(self):
        return "Employee:id:" + str(self.emp_id) + "\n" + self.emp_name + "\n" + self.emp_city + "\n" + str(self.emp_sal) + "\n"

def main(): 
    e1 = Employee(30, "xyz", "pqr", 10000)
    e2 = Employee(20, "xyz", "pqr", 10000)
    e3 = Employee(10, "xyz", "pqr", 10000)
    e4 = Employee(50, "xyz", "pqr", 10000)
    e5 = Employee(11, "xyz", "pqr", 10000)
    empL = [e1, e2, e3, e4, e5]
    for x in empL: 
        print(x)
    empL.sort() 
    print("-" * 80)
    for x in empL: 
        print(x)

main()