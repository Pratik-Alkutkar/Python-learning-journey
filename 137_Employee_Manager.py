class Employee: 
    def __init__(self, emp_id, emp_city): 
        self.emp_id = emp_id 
        self.emp_sal = 25000
        self.emp_city = emp_city 

    def get_id(self): 
        return self.emp_id 
    
    def get_salary(self): 
        return self.emp_sal 
    
    def get_city(self): 
        return self.emp_city 
    
class Manager(Employee): 
    def __init__(self, mng_id, mng_city, mng_team_size): 
        Employee.__init__(self, mng_id, mng_city)
        self.team_size = mng_team_size 

    def get_salary(self): 
        emp_sal = Employee.get_salary(self)
        mng_sal = emp_sal + 0.1 * emp_sal 
        return mng_sal 
    
    def get_team_size(self): 
        return self.mng_team_size 
    
def main(): 
    M = Manager(25, "Pune", 15)
    print("Manager ID:", M.get_id()) # Inheriter 
    print("Manager salary:", M.get_salary()) # Overridden function -> Extender 
    print("Manager City:", M.get_city()) # Inheriter 
    print("Manager team size:", M.get_team_size()) # Derived specific behaviour 

main()