Let C1 and C2 be two classes. If they are related to each other
then following is the list of possible relationships between them. 

1) DEPENDS - ON RELATIONSHIP. 

C2 DEPENDS - ON C1 (meaning?)

One of the class methods of C2 uses 
object of C1 for its implementation. 

class C1: 
    # some def 

class C2: 
    def __init__(self): 
        # constructor 

    def method(self, args): 
        st 
        st 
        st 
        objC1 = C1(data)
        objC1.c1_methods() 

        st 
        st 
        st 

class Date: 
    def __init__(self, dd, mm, yy): 
        self.dd = dd 
        self.mm = mm 
        self.yy = yy 

    def __str__(self): 
        date_str = str(self.dd) + "-" + str(self.mm) + "-" + str(self.yy)
        return date_str 

D = Date(1, 2, 1970)
print(D) # 1-2-1970

Date depends on str 
#-----------------------------------------------------------------------------

2) Class C2 has a C1 
    If object of class C2 contains object of class C1 
    then C2 has a C1 is True 

    One of the attributes of object C2 is attached 
    to object of type C1 

class C2: 
    def __init__(self, args): 
        self.attr1 = val1 

        self.attr_k = C1(data)

        self.attr_n = valn 

C2 has a C1 

class Book: 
    def __init__(self, bk_name, bk_price, book_ed): 
        self.bk_name = bk_name 
        self.bk_price = bk_price 
        self.bk_ed = book_ed 

b = Book("Learning Python", 9.55, 5)

Book has a  str 
Book has a  float 
Book has a  int 

#---------------------------------------------------