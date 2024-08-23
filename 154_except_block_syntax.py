# Syntax 1 
"""
try: 
    TRY BLOCK 
except ExceptionName: 
    HANDLER 
"""

# Syntax 2 
"""
try: 
    TRY BLOCK 
except (ExceptionName1, ExceptionName2,..., ExceptionName-k):
    COMMON EXCEPTION HANLDER BLOCK OF ExceptionName1 to ExceptionName-k
"""

num = 34535 
try: 
    if type(num) != int: 
        raise TypeError("Bad type for num")
    if num < 0: 
        raise ValueError("Bad value for num")
except (TypeError, ValueError): 
    print("Type or value of num is bad ")


# Syntax 3 
# catching exception object 

"""
try: 
    BLOCK 
except ExceptionName as e: 
    print(e) # For error message
"""

# Syntax 4: 
"""
try: 
    BLOCK 
except (ExceptionName1, ExceptionName2, ..., ExceptionName-k) as e: 
    print(e)
"""
num = 34535 
try: 
    if type(num) != int: 
        raise TypeError("Bad type for num")
    if num < 0: 
        raise ValueError("Bad value for num")
except (TypeError, ValueError) as e: 
    print(e)

# Syntax 5: Generic exception handler 
"""
try: 
    BLOCK 
except: 
    GENERIC EXCEPTION HANLDER 
"""

"""
try: 
    BLOCK 
except E1: 
    E1 handler 
except E2 as e: 
    E2 handler, e contains E2 object with error data 
except (E3, E4, E5): 
    Common exception handler for exceptions E3, E4, E5 
except (E6, E7, E8, E9) as e: 
    Common exception handler for exceptions E6, E7, E8, E9
    and e will be an object of one of the exceptions 
    from E6 to E9 
except: 
    Generic exception handler 
"""
