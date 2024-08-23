# Classes with constructors 

# 1 
class Date: 
    def __init__(self, init_day:int, init_month:int, init_year:int): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year 

D = Date(1, 1, 1970)
print(D.__dict__)

#2 
class Date: 
    def __init__(self, init_day:int, init_month:int, init_year:int): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year 

D = Date(1, 1, 1970) 
print(D.__dict__)

#3 
class Date: 
    def __init__(self, init_day:int, init_month:int, init_year:int): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year 

D = Date(1, 1, 1970) 
print(D.__dict__)

#4 
class Date: 
    def __init__(self, init_day:int, init_month:int, init_year:int): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year 

D = Date(1, 1, 1970) 
print(D.__dict__)

#5 
class Date: 
    def __init__(self, init_day:int, init_month:int, init_year:int): 
        self.day = init_day 
        self.month = init_month 
        self.year = init_year 
    
D = Date(1, 1, 1970) 
print(D.__dict__)

#--------------------------------------------------------------------------------

# Class Triangle whose object access three lengths of three sides 

#1 
class Triangle: 
    def __init__(self, s1:float, s2:float, s3:float): 
        # Typechecking 
        if (s1 + s2 <= s3 or s2 + s3 <= s1 or s3 + s1 <= s2): 
            raise ValueError("Bad values")
        self.s1 = s1 
        self.s2 = s2 
        self.s3 = s3

T = Triangle(1.2, 4.3, 3.5)

#2 
class Triangle: 
    def __init__(self, s1:float, s2:float, s3:float): 
        if s1 + s2 <= s3 or s2 + s3 <= s1 or s3 + s1 <= s2: 
            raise ValueError 
        self.s1 = s1 
        self.s2 = s2 
        self.s3 = s3 

T = Triangle(1.2, 4.3, 3.5)

# 3 
class Triangle: 
    def __init__(self, s1:float, s2:float, s3:float): 
        if s1 + s2 <= s3 or s2 + s3 <= s1 or s3 + s1 <= s2: 
            raise ValueError 
        self.s1 = s1 
        self.s2 = s2 
        self.s3 = s3 

T = Triangle(1.2, 4.3, 3.5)

#4 
class Triangle: 
    def __init__(self, s1:float, s2:float, s3:float): 
        if s1 + s2 <= s3 or s2 + s3 <= s1 or s3 + s1 <= s2: 
            raise ValueError 
        self.s1 = s1 
        self.s2 = s2 
        self.s3 = s3 

T = Triangle(1.2, 4.3, 3.5)

#5 
class Triangle: 
    def __init__(self, s1:float, s2:float, s3:float): 
        self.s1 = s1 
        self.s2 = s2 
        self.s3 = s3 

T = Triangle(1.2, 4.3, 3.5)

#----------------------------------------------------------------

# class layout for singly linked list 

# 1 
class snode: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 

class singly_linked_list: 
    def __init__(self): 
        self.head_node = snode() 

SL = singly_linked_list() 

# 2 
class snode: 
    def __init__(self, data = None): 
        self.data = data 
        self.next = None 

class singly_linked_list: 
    def __init__(self): 
        self.head_node = snode()

SL = singly_linked_list() 

# 3 
class snode: 
    def __init__(self, data = None): 
        self.data = data 
        self.next = None 

class singly_linked_list: 
    def __init__(self): 
        self.head_node = snode() 

SL = singly_linked_list() 

# 4 
class snode: 
    def __init__(self, data = None): 
        self.data = data 
        self.next = None 

class singly_linked_list: 
    def __init__(self): 
        self.head_node = snode() 

SL = singly_linked_list() 

# 5 
class snode: 
    def __init__(self, data = None): 
        self.data = data 
        self.next = None 

class singly_linked_list: 
    def __init__(self): 
        self.head_node = snode() 

SL = singly_linked_list()

# Node layout Doubly linked list 

#1 
class dnode: 
    def __init__(self, data = None): 
        self.data = data 
        self.prev = None 
        self.next = None 

class doubly_linked_list: 
    def __init__(self): 
        self.head_node = dnode() 

DL = doubly_linked_list() 

# 2 
class dnode: 
    def __init__(self, data = None): 
        self.data = data 
        self.prev = None 
        self.next = None 

class doubly_linked_list: 
    def __init__(self): 
        self.head_node = dnode() 

DL = doubly_linked_list() 

#3 
class dnode : 
    def __init__(self, data = None): 
        self.data = data 
        self.prev = None 
        self.next = None 

class doubly_linked_list: 
    def __init__(self): 
        self.head_node = dnode() 

DL = doubly_linked_list() 

# 4 
class dnode: 
    def __init__(self, data = None):
        self.data = data 
        self.prev = None 
        self.next = None 

class doubly_linked_list: 
    def __init__(self): 
        self.head_node = dnode() 

DL = doubly_linked_list() 

# 5 
class dnode: 
    def __init__(self, data = None): 
        self.data = data 
        self.prev = None 
        self.next = None 

class doubly_linked_list: 
    def __init__(self): 
        self.head_node = dnode() 

DL = doubly_linked_list() 

#----------------------------------------------------

# Binary search tree layout 

#1 
class bst_node: 
    def __init__(self, data = None): 
        self.data = data 
        self.left = None 
        self.right = None 
        self.parent = None 

class bst: 
    def __init__(self): 
        self.root_node = bst_node() 

T = bst() 

# 2 
class bst_node: 
    def __init__(self, data = None): 
        self.data = data 
        self.left = None 
        self.right = None 
        self.parent = None 

class bst: 
    def __init__(self): 
        self.root_node = bst_node() 

T = bst() 

# 3 
class bst_node: 
    def __init__(self, data = None): 
        self.data = data 
        self.left = None 
        self.right = None 
        self.parent = None 

class bst: 
    def __init__(self): 
        self.root_node = bst_node() 

T = bst() 

# 4 
class bst_node: 
    def __init__(self, data = None): 
        self.data = data 
        self.left = None 
        self.right = None 
        self.parent = None 

class bst: 
    def __init__(self): 
        self.root_node = bst_node()

T = bst() 

# 5 
class bst_node: 
    def __init__(self, data = None): 
        self.data = data 
        self.left = None 
        self.right = None 
        self.parent = None 

class bst: 
    def __init__(self): 
        self.root_node = bst_node() 

T = bst() 

