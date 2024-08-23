def insertion_sort(L:list): 
    if type(L) != list: 
        raise TypeError("L must be a list")
    j = 1 
    while j < len(L): 
        key = L[j]
        i = j - 1 
        while i > -1 and L[i] > key: 
            L[i+1] = L[i]
            i = i - 1 
        L[i+1] = key 
        j = j + 1 
#---------------------------------------------------

L = [40, 20, 10, 30, 60, 50, 70]
print("Before sort:L:", L)
insertion_sort(L)
print("After sort:L:", L)

#--------------------------------------------------------

class SortClass: 
    def __init__(self, sort_func): 
        self.sort_function = sort_func 

    def __call__(self, lst): 
        self.sort_function(lst)

    def set_sort_method(self, new_sort_func): 
        self.sort_function = new_sort_func

s = SortClass(insertion_sort)
print("type(s):", type(s))
L = [3, 6, 1, 9, 6, 2, 4, 7]
print("Before sort():", L)
s(L) # SortClass.__call__(s, L)
print("After sort():", L)

#----------------------------------------------

class Date: 
    def __init__(self, init_day, init_month, init_year): 
        print("self.__dict__", self.__dict__) # {} 
        self.day = init_day # {'day':1}
        print("self.__dict__:", self.__dict__) # {'day':1}
        self.month = init_month 
        print("self.__dict__:", self.__dict__) # {'day':1, 'month':2}
        self.year = init_year 
        print("self.__dict__:", self.__dict__) # {'day':1, 'month':2. 'year':1970}