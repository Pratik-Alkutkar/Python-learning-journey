Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class X:
    a = 10
    b = 20
    c = a + b
    L = [10, 20, 30]
    def func():
        print("IN X.func()")

        
X.__dict__
mappingproxy({'__module__': '__main__', 'a': 10, 'b': 20, 'c': 30, 'L': [10, 20, 30], 'func': <function X.func at 0x000001788D267D90>, '__dict__': <attribute '__dict__' of 'X' objects>, '__weakref__': <attribute '__weakref__' of 'X' objects>, '__doc__': None})
objX = X()
objX.__dict__
{}
steps = """objX = X()
s1: Python understands that this is an assignment statement. Therefore, Python executes an RHS first.
s2: RHS = X(). Python first analyses type of object X is naming. Because it could be a function,
it could be a class or it could be other callable object. (we have not covered callable object yet)
type(X) == class function or class builtin_function_or_method == X is a function
type(X) == class type == X is a class
Otherwise X is a other type of callable object"""
steps = """
s3: If X is a class then Python allocates a new object.
    i) type component of a new object is initialised to class X
    ii) Ref count is zero
    iii) Value component contains an empty dictionary.
s4: Newly allocated object in s3 is assigned to LHS variable objX and therefore,
    ref count shifts from zero to one.
s5: If objX.__dict__ is printed, it would be an empty dictionary.
"""

