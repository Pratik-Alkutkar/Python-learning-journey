My Python learning journey's path right from low-level to high-level applications.  

Part 1: The Python Programming Language: Basic

--> The programming fundamentals:
o The brief overview of computer and computer programming.
o Introduction to computer languages – low level languages: the machine language and assembly language – The high-level programming languages – Python programming languages.
o What is computing? What is data? What is algorithm? What is data type? What is IO? What is system service? What is library/package? What is software development kit?
--> The Python as a Software Development Kit.
o The standard Python SDK.
o Anaconda SDK for Machine Learning.
o Flask package for web development.
o Packages for automation.
--> The fundamentals:
o ‘Hello,World’ program.
o Structure of Python program: Package/module, class statement, def statement.
o Assignment statement – Fundamental ways to create data and manipulate data.
o Internal format of object in Python – Type, value, reference count.
o Garbage collection.
o Concept of variable name. Concept of operators. Coverage of arithmetic and logic operators. Aray of operator. Prefix, infix, and postfix operators. Left to right and right to left associative operators. Relative precedence of operators.
--> Branching and looping statements:
o Control flow of Python program.
o Block structure and indentation level of Python syntax.
o What are conditions and how to write conditions in Python?
o Conditional execution in Python.
--> Branching statements:
• If statement.
• If-else statement
• If-elif-else statement
▪ Looping statement.
• For statement
• While statement
▪ Break statement
▪ Continue statement
▪ Pass statement.
o Understanding the control flow of program using flow charts. Flow chart of branching and looping statements.
--> Data Types in Depth:
o Classification:
▪ Atomic type vs container data types.
▪ Sequential containers. Associative containers, neither sequential nor associative containers.
▪ Mutable and immutable data type.
▪ Understanding basics of bool, int, float, str, tuple, list, dictionary, set
o Atomic data types in depth:
▪ Learning to create and process Boolean, int and float objects.
▪ Logical not, logical and, logical or operators.
▪ Arbitrary precision integer arithmetic in Python.
▪ Integer division and floating-point division operator.
▪ Exponential Operator.
o Container data type operations in depth:
▪ Str: concatenation, multiplication by scaler, membership testing, index, range, slice, index(), count(), strip(), lstrip(), rstrip(), split(), rsplit(), format(), isalpha(), isdigit(), isalnum(), isnumeric(), istitle(), isspace(), isprintable(), partition(), rpartition(), join()
▪ List: concatenation, multiplication by scaler, index, range, slice, membership testing using ‘in’ operator, index assignment, range assignment, slice assignment, index deletion, range deletion, slice, deletion, index(), count(), append(), extend(), insert(), remove(), pop(), clear(), copy(), sort(), reverse()
▪ Tuple: concatenation, multiplication by scaler, index, range, slice, membership testing using ‘in’ operator, index(), count()
▪ Dict: adding key-value pair in dictionary, editing value of a given key, removing key-value pair in dict, keys(), values(), items(), pop(), popitem(), clear(), copy(), update(), fromkeys(), get(), sefdefault()
▪ Set: Membership testing using ‘in’ operator, union(), intersection(), difference(), symmetric_difference(), update(), intersection_update(), difference_update(), symmetric_difference_update(), issubset(), issuperset(), isdisjoint(), add(), remove(), discard(), pop(), clear(), copy().
• The Procedural Programming using Def statement:
o Writing a new algorithm. Input of an algorithm. Output of an algorithm.
o Writing reusable code using procedure. Formal parameters of a procedure. Actual parameters of a procedure. Return value of a procedure. Definition of a procedure. Call of a procedure.
o The def statement in Python as a means of writing new procedure.
o Internal processing of def statement: the function object, the code object, Python Virtual Machine (PVM) code. What function definition creates in memory? How is code object stored inside function object? How is code object stored inside object executed?
o Calling a procedure. Pass by reference mechanism used by Python.
o Global and local variables. Observing global and local symbol table by globals() and locals() functions.
o Nested def statement: Writing def statement inside def statement. Tracing control of a program having nested def statements. Looking at the memory allocation details of a nested procedure.
o Scope-visibility-lifetime model of Python:
▪ Introducing four scopes in Python viz. local, enclosing, global and builtin.
▪ Understanding LHS variable name processing.
▪ Understanding LEGB scope rule of RHS variable lookup.
▪ Unbound local error: cause and fix.
▪ Free variable error: cause and fix.
▪ Global statement
▪ Nonlocal statement.
o Implicit state saving and function factory design pattern.
o Parameter passing:
▪ Non-keyword and keyword syntax of sending specifying actual parameters.
--> Six types of formal parameters:
• Positional arguments
• Keyword arguments
• Extra nonkeyword arguments
• Default arguments
• Keyword only arguments
• Extra keyword arguments
• *args, **kwargs technique
o Static namespace of function. Function.__code__, function.__name__, function.__dict__
• Functional Programming:
--> List comprehension:
▪ Basic list comprehension of single variable
• adding a filter condition to a comprehension
• adding function to a comprehension, adding condition and
• function simultaneously to list comprehension.
▪ Multivariable list comprehension:
• cartesian product.
• computing simple two variable comprehension, generalizing to n variables.
• adding condition to two variable and generalized comprehension.
• adding function to two variable and generalized on comprehension.
• applying filter condition on the result of comprehension.
--> Lambda Expression:
▪ Lambda expression to create an anonymous function object.
▪ Formal parameters to lambda expression.
▪ Writing a definition lambda expression using its formal parameters, already defined variables and constant expression
▪ Using lambda expression.
o Map Class: Learning to apply a common function on all elements in iterables.
o Filter Class: Learning to apply a filter condition on all elements in iterables.
o Reduce function: Reduce iterable to a single object by repeatedly performing operation on elements of the iterable.
o The yield statement and generator object. Next method on generator object.
o Functools package in depth.

Part 2: Application Development

--> An overview of standard Python package repository.
o The import statement and its variations. Import package, from package import attribute, from package import attribute as alias.
o Package names look up and the PYTHONPATH
o Systematic handling of package hierarchy.
--> The ‘os’ and ‘sys’ package.
o The high-level file handling: Learning to open, create, read, write, and close file using high level file API’s. Developing file utilities: copy command, word count command, cat command.
o File attributes: Obtaining stat information about file.
--> Directory management:
▪ Get present working directory
▪ change present working directory.
▪ Listing files in the current directory.
▪ Recursively walking through the directory.
▪ Removing files from directory. Removing directory. Renaming file. Renaming directory.
--> Process management:
▪ Creating child process. Os.fork()
▪ Exchanging data between the child and the parent process.
▪ Loading a new program in a newly created process. Os.exeve()
▪ The parent child synchronization. Os.wait()
▪ Termination of a process. Os.exit()
--> Thread management:
▪ Creating new threads.
▪ Exchanging data between the child and the parent thread
▪ Joining with the child thread
▪ Detaching with the child thread
▪ The thread synchronization mechanisms
▪ Termination of a thread.
• Data persistence and the database connectivity:
--> The pickle package. dump () and load () methods.
o DBM files: Files, portability and close.
--> Shelve files: Storing built in object types in Shelves, storing class instances in shelve.
--> Sqlite3 connectivity.
• The regular expression package.
• XML and HTML parsing
• JSON parsing.

Part 3: Python Programming Language: Advanced

--> Object Oriented Programming in Python:
--> The class statement:
▪ Writing class statement. The root class ‘type’ in Python.
▪ Writing constructor of a class __init__()
▪ Creating an object from a class.
▪ Adding a class method to a class.
▪ Adding a static method to a class.
▪ Implementing various types to practice class statement.
--> Operator overloading:
▪ Overloading arithmetic and logic operators: __add__(), __sub__(), __mul__(), __truediv__(), __floordiv__(), __mod__(), __and__(), __or__(), __abs__(), __pow__
▪ Overloading advanced operators:
• Overloading [] operator with __getitem__(), and __setitem__()
• Overloading () operator with __call__()
▪ Operating overloading for built in functions:
• __str__, __repr__ for print()
• __len__() for len()
--> Inheritance:
▪ Principle of extensibility and reusability in software engineering.
▪ Inheritance to achieve reusability.
▪ Deriving one class from another. The base class and the derive class.
▪ Inheriting a method of base class.
▪ Overriding a method of base class for extending purpose.
▪ Overriding a method of base class for replacing purpose.
▪ The principle of information hiding and data encapsulation.
▪ The principle of polymorphism.
▪ Creating an abstract method with abstracmethod decorator in abc package.
▪ Creating an interface with abc.ABCMeta and the abstractmethod decorator.
▪ The root base class, class object.
▪ Obtaining base classes of a given class with __bases__
▪ Method resolution order: __mro__
▪ Multi-level inheritance
▪ Multiple inheritance
▪ Multiple inheritance and the diamond problem.
--> Exception Handling:
▪ What are exceptions? Need for an exception.
▪ Built in exceptions: NameError, ValueError, TypeError, UnboundLocalError, LookupError, FileNotFoundError, PermissionError, ModuleNotFoundError etc.
▪ Handling exception using try-except statement.
▪ Handling multiple exceptions using single except block
▪ Fetching exception information with ‘as’ clause.
▪ Writing generic exception handler block.
▪ Try-except-else statement
▪ Try-except-finally statement
▪ Try-except-else-finally statement
▪ Raise an exception using raise statement. Three ways to write a raise statement.
▪ Following most derived to most base order while handling multiple exceptions in common inheritance hierarchy.
▪ Defining an exception of one’s own.
▪ Fetching last raised exception information with sys.exc_info()
▪ Assert statement
--> Advanced Python Programming and Design patterns:
--> The Iterator Design Pattern:
▪ Understanding expansion of for loop into while loop.
▪ Understanding __iter__() method.
▪ Understanding Type_Iterator class.
▪ Understanding __next__() method
▪ Iterator with read semantics.
▪ Iterator with consumer semantics.
▪ Writing iterators on our own.
o The context management protocol:
▪ The with statement. The as clause.
▪ __enter__() for post construction initialization.
▪ __exit__() : a handler before destruction.
▪ Achieving automatic acquire, use, release cycle with context management protocol.
▪ Writing __exit__() method properly to handle unhandled exception in the with block.
--> The decorator design pattern:
▪ Python as a language of hooks.
▪ An overview of hooking techniques in Python.
▪ Function decorating a function.
▪ Function decorating a class.
▪ Class decorating a function.
▪ Class decorating a class.
o Attribute Management:
▪ Attribute management using property class. Fget, fset, fdel attributes of property class. Getter(), setter(), delete() methods on property objects. Creating a managed attributed using property class.
--> The descriptor protocol:
• Creating a reusable managed attribute using a descriptor class.
• __get__() method. __set__() method. __delete__() method
▪ Manging attribute by using non-existent attribute: __getattr__(), __setattr__(), __delattr__()
▪ Managing attributes method #4: __getattribute__(), __setattr__(), __delattr__()
--> Metaclass:
▪ Hooking class creation using metaclass.
▪ Type.__call__ method.
▪ Type.__new__ method.
▪ Metaclass as a derived class of the root class type.
▪ Overriding __new__() in metaclass to extend type.__new__()
▪ Overriding __call__ in metaclass to extend type.__call__()
▪ Implementing our own abstract base class meta.

Part 4: Machine Learning:

--> The Numpy Library: introduction
o Ndarray: The heart of the library
▪ Create an array
▪ Types of data
▪ The dtype option
▪ Intrinsic creation of an Array
o Basic Operations:
▪ The arithmetic operators
▪ The Matrix product
▪ Increment and Decrement operators
▪ Universal Functions (ufunc)
▪ Aggregate functions
o Indexing, slicing, and iterating
o Conditions and Boolean Arrays
o Shape manipulation
--> Array manipulation: Joining and splitting Arrays
o Copies of views of object
o Vectorization
o Broadcasting
o Structured Arrays
o Reading and Writing data on binary files
--> The panda’s library: introduction
o Introduction to Pandas data structure
▪ The series
▪ The data frame
▪ The index objects
o Other functionalities on indexes: Reindexing – Dropping – Arithmetic and data alignment
o Operations between data structures: Flexible arithmetic methods, operations between DataFrame and Series
o Function application by Mapping – Function by element – Functions by row or column, statistics function
o Sorting and ranking
o Correlation and Covariance
o Non a Number data: Assigning a NaN value – Filtering out NaN values – Filling in NaN occurrences.
• Pandas: IO
o I/O API tools
--> CSV and textual files
▪ Reading data in CSV or text files: Using RegExp to pars TXT files
▪ Reading TXT files into Parts
▪ Writing Data in CSV
o Reading and writing HTML files: Writing data in HTML, Reading data from HTML
file
o Reading and writing data from XML files
o Reading and Writing data on Microsoft Excel files
o JSON data.
--> Data visualization with matplotlib
--> The matplotlib architecture: Backend layer, Artist layer, Scripting Layer, pylab
and pyplot
o A simple interactive window with pyplot.
o The plotting window: set properties of the plot. Matplotlib and Numpy
o Using kwargs: Working with multiple figures and axes
--> Adding elements to the Chart: Adding text – Adding a grid – Adding a Legend
o Saving charts: Saving a code – Converting session into an HTML files – Saving as
an image
o Handling Date values
o Chart Typology
o Lines chars
o Histograms
o Bar Charts – Horizontal bar charts – Multi serial bar charts – Multiseries bar with
pandas DataFrame
o Multiseries Stacked Bar Charts
o Pie chart
--> Advanced charts: Contour plots, polar plots
--> The mplot3d toolkit: 3D surfaces, scatter plots in 3D, Bar charts in 3D
--> Machine Learning with scikit-learn
o The scikit-learn library
--> Machine Learning – Supervised and Unsupervised Learning
o Supervised learning with scikit-learn
o The iris flower data-set – The PCA Decomposition
o K-Nearest Neighbour classifier
o Diabetes dataset
o Linear regression: the least square regression
o Support Vector Machines (SVMs)
▪ Support Vector Classification (SVC)
▪ Nonlinear SVC
▪ Plotting Different SVS classifiers using Iris data set
• Textual data analysis with NLTK:
o The natural language toolkit – NLTK
o Search for a word with NLTK
o Analyze the frequency of words
o Selection of words from text
o Bigrams and Collocations
• Introduction to Deep Learning with TensorFlow.

Part 5: Web development using Flask

--> Basic application structure – Initialization, Routes and view functions, server start – up, a request response cycle, a Flask hello, world application
• Templates – The Jinja 2 template engine, Custom error pages, links, static files, localization of dates and times
• Webforms – Cross site request forgery, Form classes, HTML of rendering forms, Form handling in view functions, Redirects and user sessions, Message flashing.
• Databases
• Email support
--> Large application structure – Project structure, configuration options, Application package, launch script, requirement files, unit tests, database setup

Part 6: Automation

• File automation: All topics are covered in file handling part of ‘os’ and ‘sys’ module. 
• Process & thread automation: All topics are covered in file handling part of ‘os’ and ‘sys’ module.
• Regular Expression: All topics are covered in file handling part of ‘os’ and ‘sys’ module.
• String manipulation: Covered in Part 1: The Python Programming Language
--> Web scrapping with BeautifulSoup:
o The request module
o Attributes and navigation
o Accessing attributes and contents
o Sibling, elements, and children
• Handling data file formats: Excel, Word, JSON (Already covered in pandas)
--> GUI Automation with PyWinAuto.
--> GUI Automation with PyAutoGui.  
