# If a varaible name is used on LHS on current line then 

# Step 1: Find out the scope of current line and locate the symbol table 
# of the current line. 

# Step 2: Search variable name used on LHS in the symbol table. 
# If not found -> conclude that variable name is used on LHS for the first time 
# [DEFINITION CASE]
# If found -> conclude that variable has been used on LHS before in the current scope 
# [RE-ASSIGNMENT CASE] 

# Step 3:
#   if DEFINITION CASE: Then create a new entry symbol table and store 
#   variable name in string form as a key and id of RHS object as value 
#   in it. Increment the ref count of RHS object by 1 

#   if RE-ASSIGNMENT CASE: Do not create a new symbol table entry, 
#   rather use the existing one. Replace id of 'old' object 
#   by the id of object created by current RHS. Decrement the ref count 
#   of 'old' object by 1. If it falls down to zero then invoke garbage collector 
#   to clear it. Increment the reference count of current RHS object by 1. 

