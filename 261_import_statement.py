"""
import package_name 

1) A file name package_name.py is formed. 
2) A file is searched the CURRENT WORKING directory of a 
    process which has imported the package. If it is found 
    then go to step 4. If not found go to step 3 
3) Search for the file in directory path present in 
    PYTHON_PATH variable. If found then go to step 4 
    If not found -> raise ModuleNotFoundError -> STOP 
4) Execute the file package_name.py. 
    All functions(class function objects), classes (
    class type objects), constants (other data objects)
    that are defined in the module are allocated in 
    program memory of a program which is importing the module. 
5) An object of type class module is allocated in the program 
    memory of program importing module. 

    All things (functions, classes, data objects) that are 
    defined in module are stored in dictionary inside the 
    object of type class module. 
"""

"""
package_name.py 

def func(): 
    some logic 

class MyType: 
    # some def 

N = 100 

#-------------------------------------
app.py 

import package_name 

# rest of the application 

#------------------------------------------

# python app.py


"""