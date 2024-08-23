def is_prime(n:int)->bool:
    '''
    @input:
    @n: int: an integer whose prime-ness will be tested
    @output:
    True or False depending on whether n is prime.
    '''
    if n == 1:
        return False
    if n == 2:
        return True

    flag = True
    k=2
    while k < n:
        if n % k == 0:
            flag = False
            break
        k = k + 1
    return flag


'''
TODO:   Write a main function. Print numbers from 1 to 100 along with 
        their result of prime test 
'''