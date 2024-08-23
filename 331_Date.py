class Date: 
    def __init__(self, dd, mm, yy): 
        self.dd, self.mm, self.yy = dd, mm, yy 

D = Date(1, 1, 1970)

"""
Date:type object 

D = Date(1, 1, 1970)
Assignment statement: 
    EXECUTE RHS 
    Date(1, 1, 1970)
    LOOK UP FOR VARIALBE Date in symbol table 
    FOUND. 
    DATE IS ASSOCIATED WITH OBJECT OF class type 
    Date()==class type chya object war call operator takne

    type.__call__(Date, 1, 1, 1970)
        type.__new__(Date)
            NEW OBJECT IS ALLOCATED 
            ITS type field will contain class Date 
            ITS reference count will be zero 
            ITS value component will be an empty dict
            return newly created object to type.__call__ 
        
        Back to type.__call__: new_obj will contain a new object 
        returned by type.__new__ 

        Does Date class have a constructor? 
        YES 
        new_obj = Date.__init__(new_obj, *args)
        Does Date class have __enter__? 
        NO 
        return new_obj 

D == new_obj 



"""