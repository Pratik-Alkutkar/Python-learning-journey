def is_year_leap(y:int)->bool: 
    '''
    @input: y: Year 
    @output: True if y is leap, False otherwise    
    '''
    if y % 4 == 0 and y % 100 != 0:
        return True 
    elif y % 4 == 0 and y % 100 == 0 and y % 400 == 0: 
        return True 
    else: 
        return False 

def is_date_valid(day:int, month:int, year:int)->bool: 
    '''
    @day: int: day
    @month: int: month 
    @year: int: year
    @return: True of day-month-year form a valid date 
    as per Gregorian Calender, False otherwise
    '''
    return (
                (
                    (month == 2) and 
                    (
                        is_year_leap(year) and day in range(1,30) or 
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