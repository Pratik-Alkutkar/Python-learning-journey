"""
@Author:    Pratik Pramod Alkutkar 
@Date:      1st Feb 2023 
@Goal:      To implement data type Date with 
            constructor and getter and setters 
            of all attributes in object 
"""

def is_year_leap(year:int)->bool: 
        '''
        @input: year: Year 
        @output: True if y is leap, False otherwise    
        '''
        return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def is_date_valid(day:int, month:int, year:int)->bool: 
        '''
        @day: int: day
        @month: int: month 
        @year: int: year
        @return: True of day-month-year form a valid date 
        as per Gregorian Calender, False otherwise
        '''
        return  (
                    (
                        (month == 2) 
                        and 
                        (
                            is_year_leap(year) and day in range(1, 30) or 
                            not is_year_leap(year) and day in range(1, 29)
                        )
                    ) or 
                    (
                        month in (1, 3, 5, 7, 8, 10, 12) and day in range(1, 32)
                    ) or 
                    (
                        month in (4, 6, 9, 11) and day in range(1, 31)
                    )
        )

class Date: 
    '''
    Implementation of class Date 
    def __init__(self, init_day, init_month, init_year)
        Construtor of class Date accepting three initialisation 
        parameters viz. day, month and year 
    
    def get_day(self) 
        getter of day 

    def set_day(self, new_day)
        setter of day 

    def get_month(self)
        getter of month 

    def set_month(self, new_month) 
        setter of month 

    def get_year(self)
        getter of year 

    def set_year(self, new_year)
        setter of year 

    def show(self)
        prints date in day-month-year format
    '''
    def __init__(self, init_day:int, init_month:int, init_year:int): 
        '''
        Construtor function 
        @init_day: initialisation value for day 
        @init_month: initialisation value for month 
        @init_year: initialisation value for year 
        '''
        # type checking 
        if type(init_day) != int or type(init_month) != int or type(init_year) != int: 
            raise TypeError("day, month, and year must be integers")
        
        # value checking 
        if not is_date_valid(init_day, init_month, init_year): 
            raise ValueError("%d-%d-%d don't form valid date as per Gregorian calender" % 
                        (init_day, init_month, init_year))

        self.day = init_day 
        self.month = init_month 
        self.year = init_year 

    def get_day(self)->int: 
        '''
        get_day(self)
            getter of day 
        '''
        return self.day 

    def set_day(self, new_day:int)->None: 
        '''
        set_day(self, new_day)
            sets day to new_day after passing validation
        '''
        # type check 
        if type(new_day) != int: 
            raise TypeError("new_day must be an integer")
        # value check 
        if not is_date_valid(new_day, self.month, self.year): 
            raise ValueError("%d-%d-%d do not form valid date" % 
                            (new_day, self.month, self.year))
        self.day = new_day 

    def get_month(self)->int: 
        '''
        get_month(self)
            getter of month 
        '''    
        return self.month 

    def set_month(self, new_month:int)->None: 
        '''
        set_month(self, new_month)
            sets month to new_month after passing validation check 
        '''
        # type check 
        if type(new_month) != int: 
            raise TypeError("new_month must be an integer")
        # value check
        if not is_date_valid(self.day, new_month, self.year): 
            raise ValueError("%d-%d-%d do not form valid date" % 
                            (self.day, new_month, self.year))

        self.month = new_month

    def get_year(self)->int: 
        '''
        get_year(self)
            getter of year
        '''
        return self.year 

    def set_year(self, new_year:int)->None: 
        '''
        set_year(self, new_year)
            sets year to new_year 
        '''
        # type check 
        if type(new_year) != int: 
            raise TypeError("new_year must be an integer")
        self.year = new_year 

    def show(self)->None: 
        '''
        show(self)
            prints date in day-month-year format
        '''
        print("%d-%d-%d" % (self.day, self.month, self.year))

def main(): 
    print("TEST: D = Date(1, 2, 2023)")
    D = Date(1, 2, 2023)
    D.show() 

    try: 
        print("TEST: D = Date(1.1, 4.5, -102.3)")
        D = Date(1.1, 4.5, -102.3)
    except TypeError as e: 
        print(e)

    try: 
        print("TEST: D = Date(29, 2, 1977) ")
        D = Date(29, 2, 1977)
    except ValueError as e: 
        print(e)

    try: 
        print("TEST: D = Date(34, 2, 1977) ")
        D = Date(34, 2, 1977)
    except ValueError as e: 
        print(e)

    try: 
        print("TEST: D = Date(1, 25, 1977)")
        D = Date(1, 25, 1977)
    except ValueError as e: 
        print(e)

    try: 
        print("TEST: D = Date(31, 6, 1977) ")
        D = Date(31, 6, 1977)
    except ValueError as e: 
        print(e)

main() 
