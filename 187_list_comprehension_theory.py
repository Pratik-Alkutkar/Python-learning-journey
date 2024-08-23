Explanation: 
do_squats for 15 mins

HOD -> class teacher

keep_record for every student in class

# General Syntax:
# version 1 
L = [v_name for v_name in iterable]
# version 2
L = [f(v) for v in iterable]
# version 3
L = [v for v in iterable if cond(v)]
How to evaluate version 3:
    Step 1: Split the iterable into its constituent elements
    Step 2: Apply cond after if, on each element generated in
            Step 1. Select only those for which cond evaluated
            to True, discard all for which cond evaluated to False
    Step 3: Make a list of all elements selected in Step 2

L = [x for x in range(10) if x % 2 == 0]

Step 1: Split iterable:
        iterable = range(10)
        after splitting, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

Step 2: Apply cond:
        0 % 2 == 0 : T 
        1 % 2 == 0 : F 
        2 % 2 == 0 : T 
        3 % 2 == 0 : F 
        4 % 2 == 0 : T 
        5 % 2 == 0 : F 
        6 % 2 == 0 : T 
        7 % 2 == 0 : F 
        8 % 2 == 0 : T 
        9 % 2 == 0 : F

        Select only those for which cond evaluated to True
        0, 2, 4, 6, 8

Step 3: Make list of elements selected in Step 2
        [0, 2, 4, 6, 8] 

# Version 4:
L = [f(v) for v in iterable if Cond(v)]
How to evaluate version 4:
    Step 1: Split the iterable into its constituent elements
    Step 2: Apply cond after if, on each element generated in
            Step 1. Select only those for which cond evaluated
            to True, discard all for which cond evaluated to False
    Step 3: Make a temporary list of all elements selected in
            Step 2. Apply function f on each element and get the
            return value.
    Step 4: Make a list of all return values in Step 3. 

Example for version 4 
L = [x**2 for x in range(10) if x % 2 == 0]
Step 1: Split iterable:
        iterable = range(10)
        after splitting, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

Step 2: Apply cond:
        0 % 2 == 0 : T 
        1 % 2 == 0 : F 
        2 % 2 == 0 : T 
        3 % 2 == 0 : F 
        4 % 2 == 0 : T 
        5 % 2 == 0 : F 
        6 % 2 == 0 : T 
        7 % 2 == 0 : F 
        8 % 2 == 0 : T 
        9 % 2 == 0 : F

        Select only those for which cond evaluated to True
        0, 2, 4, 6, 8

Step 3: Make a temporary list of elements selected in Step 2
        tmp_lst == [0, 2, 4, 6, 8]
        Apply function f(x) == x**2 on each element of tmp_lst
        f(0) == 0
        f(2) == 4
        f(4) == 16
        f(6) == 36
        f(8) == 64

Step 4: Make a final list of return values generated in Step 3
        [0, 4, 16, 36, 64] 

HOMEWORK:
Use list comprehension to generate a list containing
factorials of all prime numbers between 1 to 50.

Def : factorial: Factorial of postive integer N is defined as product of
all elements from 1 to N

Def : Prime numbers : A number is prime if its only divisors are 1 and that number.

1-> is not a prime.(no other divisor than 1)
2-> only even prime. (only divisors of 2 are, 1 and 2)
3-> prime
4 -> not prime




    
