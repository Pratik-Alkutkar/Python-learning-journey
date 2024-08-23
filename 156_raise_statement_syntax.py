# Syntax I
"""
raise ExceptionName(ExceptionData)
"""

# Syntax II 
"""
raise ExceptionName
"""

def fun(num:int)->int: 
    if type(num) != int: 
        raise TypeError
    
try: 
    fun(3.14)
except TypeError as e: 
    print("type(e):", type(e))
    print(e)

# Syntax III: 
raise 
# Meaning: re-raise the last exception! 