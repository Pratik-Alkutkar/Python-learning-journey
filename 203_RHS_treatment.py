# RHS treatment version 1: 
# If a variable name is used on RHS then look up into a symbol table 
# if found -> then use the value of object in way that is required in current rhs 
# if not found -> raise NameError exception saying that the variable name is not defined 
a = 10 
b = 20 
c = a + b 

# Revised version of RHS treatment:

# assume that variable named v is used in RHS sense. 

# 1) Find out the scope of the line where v is used on RHS 
# 2) Look up for 'v' in the symbol table associated with that scope 
# 3) If found -> use the value in the associated object in a way that is required in  RHS 
#    If not found: 
#        3-A)   Scope of Current Line: is GLOBAL 
                # then the variable name 'v' must be a BUILT IN. 
                # If yes then access the associated object from built in scope symbol table 
                # If not then raise NameError 
#        3-B)   Scope of Current Line: is LOCAL with respect to some function say f()
                # 'v' is not in local scope f() 
                # Then search symbol tables of all functions enclosing function f() 
                # in inner to outer manner 
                # If found then take object associated 'v' from that symbol table. 
                # If not found in all scopes enclosing f() then 
                # search global scope : if found there -> then take object associated with 'v' 
                # from global symbol table 
                # If not found in global symbol table as well: then check if 'v' is a built in 
                # variable name (that is check if 'v' is present in built in scope) 
                # if found -> then take object associated with from there 
                # if not found -> raise NameError exception 

