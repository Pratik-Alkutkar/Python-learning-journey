"""
for x in <iterable>: 
    # do something with x 
"""

"""
iterable 1:   something which can be iterated on. 
              logically, it must be a collection of many things put togetgher 
              logically, it must be a container data type. 

iterable 2: an object is iterable if type(object) contains a method named 
            __iter__ 

            TEST: 
            If you want to decide whether you can iterate on variable X. 

            if '__iter__' in type(X).__dict__.name(): 
                for element in X: 
                    do something with element      
"""

"""
Goal:           To create a customized iterable object. 
Illustrate:     To write a class whose object can be meaningfully used with for loop. 

Concrete Example: 
Write a class named Gensquare which will accept a POSITIVE integer. 

gs = Gensquare(N)   # where N > 0 

for x in gs: 
    print(x)    # square of all numbers from 0 to N-1 should be printed 

gs = Gensquare(5)
for x in gs: 
    print(x)    # 0, 1, 4, 9, 16

"""