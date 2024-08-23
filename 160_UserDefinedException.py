"""
Only those classes are considered as exceptions that are 
part of inheritance tree rooted at built in class Exception. 

In other words, a class C is an exception if it is 
directly or indirectly inherited from built in class Exception 

Also only those classes can be used after raise 
that are directly or indirectly inherited 
from Exception 
"""

import sys 

class UsageError(Exception): 
    pass 

def main(argc, argv): 
    if argc != 2: 
        raise UsageError("%s file_name" % argv[0])
    
main(len(sys.argv), sys.argv)