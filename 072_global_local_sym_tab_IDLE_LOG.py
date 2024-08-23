Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>}
global_sym_tab = globals()
print(global_sym_tab)
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'global_sym_tab': {...}}
type(global_sym_tab)
<class 'dict'>
n = 10
globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'global_sym_tab': {...}, 'n': 10}
id(n)
1740127470096
f = 3.14
globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'global_sym_tab': {...}, 'n': 10, 'f': 3.14}
def func():
    print("Inside func()")

    
globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'global_sym_tab': {...}, 'n': 10, 'f': 3.14, 'func': <function func at 0x0000019529E77D90>}
class Date:
    pass

globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'global_sym_tab': {...}, 'n': 10, 'f': 3.14, 'func': <function func at 0x0000019529E77D90>, 'Date': <class '__main__.Date'>}
def test_func():
    print(locals())
    n = 10
    print(locals())
    f = 3.14
    print(locals())
    k = [1000, 2000, 30000]
    print(locals())

    
globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'global_sym_tab': {...}, 'n': 10, 'f': 3.14, 'func': <function func at 0x0000019529E77D90>, 'Date': <class '__main__.Date'>, 'test_func': <function test_func at 0x0000019529E95000>}
test_func()
{}
{'n': 10}
{'n': 10, 'f': 3.14}
{'n': 10, 'f': 3.14, 'k': [1000, 2000, 30000]}
globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'global_sym_tab': {...}, 'n': 10, 'f': 3.14, 'func': <function func at 0x0000019529E77D90>, 'Date': <class '__main__.Date'>, 'test_func': <function test_func at 0x0000019529E95000>}
def test_func():
    print(locals())
    n = 500
    print(locals())
    f = 2000
    print(locals())
    k = [1000, 2000, 30000]
    print(locals())

    
globals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'global_sym_tab': {...}, 'n': 10, 'f': 3.14, 'func': <function func at 0x0000019529E77D90>, 'Date': <class '__main__.Date'>, 'test_func': <function test_func at 0x0000019529E953F0>}
