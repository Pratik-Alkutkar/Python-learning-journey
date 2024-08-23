"""
try: 
    BLOCK 
except exceptionName: 
    HANDLER 
"""

""" 
try: 
    BLOCK 
except ExceptionName as e: 
    print(e) # Error message
    FURTHER HANDLER 
"""

"""
try: 
    BLOCK 
except: 
    GENERIC EXCEPTION HANDLER 
"""

"""
try: 
    BLOCK 
except E1: 
    BLOCK 
except E2: 
    BLOCK 
.
.
.
except En: 
    BLOCK 
except: 
    GENERIC EXCEPTION HANDLER 
"""