"""
try: 
    BLOCK 
except: 
    BLOCK 
finally: 
    BLOCK 
    Control flow will come here 
    no matter what 
next stmt 
"""

"""
Case 1: try block is executed without any exception 
Case 2: exception is raised while executing try block 
        but has handler in one of the except blocks. 
Case 3: exception is raised while executing try block 
        but that exception is not handled and therefore 
        application will be terminated 
"""
