Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
type(10)
<class 'int'>
type(int)
<class 'type'>
type(float)
<class 'type'>
type(bool)
<class 'type'>
type(list)
<class 'type'>
s = "582"
print(s)
582
type(s)
<class 'str'>
n = int(s)
print(n)
582
type(n)
<class 'int'>
def fun(x):
    if type(x) != int:
        raise TypeError("x must be an integer")

    
f(3.14)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f(3.14)
NameError: name 'f' is not defined
fun(3.14)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fun(3.14)
  File "<pyshell#15>", line 3, in fun
    raise TypeError("x must be an integer")
TypeError: x must be an integer
type(int)
<class 'type'>
type(float)
<class 'type'>
type(list)
<class 'type'>
type(NameError)
<class 'type'>
type(ValueError)
<class 'type'>
type(TypeError)
<class 'type'>
n = int(10)
print(n)
10
e = ValueError("List must non-empty")
type(e)
<class 'ValueError'>
print(e.args)
('List must non-empty',)
print(e)
List must non-empty
int()
0
ValueError()
ValueError()
raise ValueError
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    raise ValueError
ValueError
ValueError.__bases__
(<class 'Exception'>,)
Exception.__bases__
(<class 'BaseException'>,)
ValueError.__mro__
(<class 'ValueError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
int.__mro__
(<class 'int'>, <class 'object'>)
raise int
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    raise int
TypeError: exceptions must derive from BaseException
raise ValueError
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    raise ValueError
ValueError
