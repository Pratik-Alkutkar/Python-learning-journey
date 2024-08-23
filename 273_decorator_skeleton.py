# Function decorated by another function 
def my_decorator(F): 
    def inner_function(*args, **kwargs): 
        print("PREPROCESSING")
        ret = F(*args, **kwargs)
        print("POSTPROCESSING")
        return ret 
    return inner_function 
#-----------------------------------------------------
# Skeleton of application of decorator 
@my_decorator
def my_function(params): 
    #BODY 
#--------------------------------------------------------------- function decorated by function OVER 

# For Advanced Audience
# Skeleton of decorator with params 

def decorator_name(p1, p2, ..., pn): 
    def true_decorator(F): 
        cc_p1 = p1 
        cc_p2 = p2 


        cc_pn = pn 
        def inner_function(*args, **kwargs): 
            # create copy of p1 to pn as required in inner function as well 
            print("PREPROCESSING")
            ret = F(*args, **kwargs)
            print("POSTPROCESSING")
            return ret 
        return inner_function
    return true_decorator

# Application of decorator 

@decorator_name(dec_p1, dec_p2, ..., dec_pn)
def my_function(some_args): 
    # BODY 

#--------------------------------------------------------------- function decorated by function (with params) OVER