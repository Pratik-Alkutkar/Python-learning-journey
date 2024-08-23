"""
PROJECT 
    DEBUG VERSION 
    RELEASE VERSION 

"""
def fun(num): 
    assert type(num) in [int, float], "bad num"
    assert num >= 0, "num must be positive"

fun("Hello")

"""
How assert works intnerally 

assert cond, error_msg 

==

if not cond: 
    raise AssertionError(error_msg)
"""

"""
assert should be used in debug version and not release version
"""