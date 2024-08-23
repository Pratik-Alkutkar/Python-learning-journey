def universal_wrapper(func_object, *args, **kwargs):
    func_object(*args, **kwargs)


def combo_1(a, b, c, *args, d=100, e=200):
    print('In combo_1') 
    print(a, b, c) # pos
    print(args) # extra nonkeyword
    print(d, e) # default


def combo_2(a, b, c, *args, d=100, e=200, p, q):
    print('In combo_2') 
    print(a, b, c) # pos
    print(args) # extra nonkeyword
    print(p, q) # keyword only

def combo_3(a, b, c, *args, d=100, e=200, p, q, **kwargs):
    print('In combo_3') 
    print(a, b, c) # pos 
    print(args) # extra nonkeyword 
    print(d, e)# default 
    print(p, q)# keyword only 
    print(kwargs) # extra keyword


universal_wrapper(combo_1, 10, 20, 30, 40, 50, 60, 70, e=-200)
"""
func_object: -> combo_1
args: 10, 20, 30, 40, 50, 60, 70
kwargs: 'e':-200

Universal wrapper: args == pos+extra nonkeyword of combo_1
Universal wrapper: kwargs == default of combo_1
"""
universal_wrapper(combo_2, 10, 20, 30, 40, 50 ,60, 70, e=-200, p=1.1, q=2.2)
"""
func_object: combo_2
Universal wrapper:args == pos+extra nonkeyword of combo_2
Universal wrapper kwargs == default + keyworld only of combo_2
"""

universal_wrapper(combo_3, 10, 20, 30, 40, 50 ,60, 70, e=-200, p=1.1, q=2.2, x=True, y=False)
"""
func_object-> combo_3
universal_wrapper:args == pos + extra nonkeyword of combo_3
universal_wrapper:kwargs == default + keyword only + extra keyword of combo_3
"""