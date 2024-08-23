'''
@Author: Pratik Pramod Alkutkar
@Date: 18th Jan 2023 
@Goal:  Write a function which accepts list size 
        from end user. The must be between 1 to 15. 
        And populate the list by integers also accepted 
        from the end user. 
'''

import sys 

def get_list()->list:
    '''
    @input: None 
    @output: list of desired length and data 
    @goal: Return a list of integers of desired length 
    ''' 

    min_length = 1 
    max_length = 15 
    
    try: 
        N = int(input("Enter the length of list[1-15]:"))
        if N < min_length or N > max_length: 
            raise ValueError("Size must be between %d and %d" % (min_length, max_length))
    except ValueError as e: 
        print(e) 
        sys.exit(-1)
    except: 
        print("Unexpected error")
        sys.exit(-1)

    # You have valid N here 
    L = []
    index = 0 
    while index < N: 
        try: 
            n = int(input("Enter any integer:"))
        except ValueError as e: 
            print(e)
            sys.exit(-1)
        except: 
            print("Unexpected error")
            sys.exit(-1)
        L.append(n)
        index = index + 1 

    return (L)

def main(): 
    L = get_list() 
    print(L)

main() 
