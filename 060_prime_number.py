import sys 

def get_list_of_integers(min_length:int, max_length:int)->list:
    '''
    @input: None 
    @output: list of desired length and data 
    @goal: Return a list of integers of desired length 
    ''' 

    if type(min_length) != int or type(max_length) != int: 
        raise TypeError("min and max length parameters must have integer input values")
    
    if min_length < 0 or max_length <= 0 or min_length > max_length: 
        raise ValueError("Wrong bounds for list length")
    
    try: 
        N = int(input("Enter the length of list[%d-%d]:" % (min_length, max_length)))
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
            n = int(input("Enter any integer at index %d:" % index))
        except ValueError as e: 
            print(e)
            sys.exit(-1)
        except: 
            print("Unexpected error")
            sys.exit(-1)
        L.append(n)
        index = index + 1 

    return (L)

def is_prime(n:int)->bool: 
    '''
    @input: n: positive integer
    @output: True if n is a prime number, False if n is not a prime number
    '''
    if type(n) != int: 
        raise TypeError("Bad type for input n")
    if n <= 0: 
        raise ValueError("Bad input value for n")
    if n == 1: 
        return False 
    if n == 2: 
        return True 
    for i in range(2, n): 
        if n % i == 0: 
            return False 
    return True 

def main(): 
    L = get_list_of_integers(1, 15)
    for i in range(len(L)):
        if is_prime(L[i]) == True: 
            print("Number at index %d, %d is prime" % (i, L[i]))
    sys.exit(0) 

main()

"""
Definition: Prime Number: A positive natural number n 
is prime if its only divisors are 1 and n. 
"""

"""
if there is a divisor of of n between 2 to n-1 
then n is not prime. 

Let i be any arbitrary number between 2 to n-1

if n % i == 0: 
    return False

for i in range(2, n): 
    if n % i == 0: 
        return False 
return True  

line 78 to 81 will work if n > 2 

if n == 1: 
    return False 
if n == 2: 
    return True 
for i in range(2, n): 
    if n % i == 0: 
        return False 
return True  

"""