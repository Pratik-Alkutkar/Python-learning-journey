"""
array: Contiguous arrangement of multiple objects of same type 

int a[5]; 

a: [   ][  ][  ][  ][  ]
    0    1   2   3   4 

Size of array cannot change. 
Array -> 5 integers 
Each element in array must of type int

Goal: 
    Implement data type array, by internally using list. 
"""

class ArrayInt: 
    def __init__(self, size:int): 
        if type(size) != int: 
            raise TypeError("Bad type for array size")
        if size < 0: 
            raise ValueError("Bad value for array size")
        self.L = [] 
        for i in range(size): 
            self.L.append(0)

    def get(self, index:int)->int: 
        print("get")
        if type(index) != int: 
            raise TypeError("Bad type for index")
        if index < 0 or index >= len(self.L): 
            raise IndexError("Bad Index")
        return_val = self.L[index]
        return return_val

    def __getitem__(self, index): 
        print("__getitem__")
        if type(index) != int: 
            raise TypeError("Bad type for index")
        if index < 0 or index >= len(self.L): 
            raise IndexError("Bad Index")
        return_val = self.L[index]
        return return_val


    def set(self, index:int, val:int)->None: 
        print("set")
        if type(index) != int: 
            raise TypeError("Bad type for index")
        if type(val) != int: 
            raise TypeError("val must be integer")
        if index < 0 or index >= len(self.L): 
            raise IndexError("Index out of range")
        self.L[index] = val 

    def __setitem__(self, index:int, val:int)->None: 
        print("__setitem__")
        if type(index) != int: 
            raise TypeError("Bad type for index")
        if type(val) != int: 
            raise TypeError("val must be integer")
        if index < 0 or index >= len(self.L): 
            raise IndexError("Index out of range")
        self.L[index] = val 

    def __len__(self): 
        return len(self.L)

    def __str__(self): 
        return str(self.L)

A = ArrayInt(8)
print("A:", A)

"""
Small recap: 
    If list or array contain N elements: 
    Then valid index range is 0 to N-1

    If A is array of integers then I must be 
    able to 'get' object of at index i, 
    and I must be able to 'set' object at index i 
"""

A.set(4, 40) # general form: A.set(index, val)
n = A.get(4) # general form: n = A.get(index)

print("n==A.get(4):", n)

# A.get(index)
# ArrayInt.get(A, index)
# def get(self, index)

# A.set(index, val)
# ArrayInt.set(A, index, val)
# def set(self, index, val)

print("How to print index range of A")
for i in range(len(A)): 
    print(i) 

"""
L = [0,0,0,0,0,0,0,0]
for i in range(len(L)): 
    L[i] = (i+1) * 10
"""
print("Before:A:", A)
print("Set every element at index i of A to (i+1)*100")
for i in range(len(A)): 
    A.set(i, (i+1)*100) # 8 times set 
print("After:A:", A)

print("Indexwise printing")
for i in range(len(A)): 
    n = A.get(i) # 8 times get 
    print("Element at index %d is %d" % (i, n))

B = ArrayInt(10)

for i in range(len(B)): 
    B[i] = (i+1) * 100  # 10 times __setitem__

for i in range(len(B)): 
    n = B[i] # 10 times __getitem__
    print("Element at index %d in B is %d" % (i, n))

""" 
Let C be a sequential container data type. 
Let objC be object of C 

If you want 
objC[i] = val 
to work then 

class C: 
    def __setitem__(self, index, val): 
        self -> object of C whose index must be set 
        index -> index at which value must be set 
        val -> value to be set 

If you want 
n = objC[i] 
to work 

class C: 
    def __getitem__(self, index): 
        self->Object of C whose index value must returned 
        index -> index 

"""