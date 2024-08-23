'''Gregorian Calender'''

'''
A leap year must divisible by 4. 
If year is also divisible by 100 then it must be divisible by 400 
to be a leap year. 
'''

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

def main(): 

    y = int(input("Enter year:"))
    if is_year_leap(y): 
        print("%d is leap" % y)
    else: 
        print("%d is not leap" % y)

main()
