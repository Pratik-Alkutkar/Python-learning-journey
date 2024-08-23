# Factorial function repetition

# 1
def fact(N:int)->int:
    if type(N) != int:
        raise TypeError
    if N < 0:
        raise ValueError
    if N == 0:
        return 1
    result = 1
    for i in range(1, N+1):
        result = result * i
    return result

# 2
def fact(N:int)->int:
    if type(N) != int:
        raise TypeError
    if N < 0:
        raise ValueError
    if N == 0:
        return 1
    result = 1
    for i in range(1, N+1):
        result = result * i
    return result


# 3
def fact(N:int)->int:
    if type(N) != int:
        raise TypeError
    if N < 0:
        raise ValueError
    if N == 0:
        return 1
    result = 1
    i = 2
    while i <= N:
        result = result * i
        i = i + 1
    return result

# 4
def fact(N:int)->int:
    if type(N) != int:
        raise TypeError
    if N < 0:
        raise ValueError
    if N == 0:
        return 1
    result = 1
    i = 2
    while i <= N:
        result *=  i
        i += 1
    return result

# 5
def fact(N:int)->int:
    if type(N) != int:
        raise TypeError
    if N < 0:
        raise ValueError
    if N == 0:
        return 1
    result = 1
    for i in range(2, N+1):
        result *= i
    return result 

#-------------------------------------------

# 1 
def prn_odd_even(L:list)->None:
    if type(L) != list:
        raise TypeError
    for x in L:
        if type(x) != int:
            raise TypeError
        if x % 2 == 0:
            print(x, "is even")
        else:
            print(x, "is odd")

# 2
def prn_odd_even(L:list)->None:
    if type(L) != list:
        raise TypeError
    for x in L:
        if type(x) != int:
            raise TypeError

        if x % 2 == 0:
            print(x, "is even")
        else:
            print(x, "is odd")

# 3
def prn_odd_even(L:list)->None:
    if type(L) != list:
        raise TypeError
    for x in L:
        if type(x) != int:
            raise TypeError

        if x % 2 == 0:
            print(x, "is even")
        else:
            print(x, "is odd")

# 4
def prn_odd_even(L:list)->None:
    if type(L) != list:
        raise TypeError
    for x in L:
        if type(x) != int:
            raise TypeError
        if x % 2 == 0:
            print(x, "is even")
        else:
            print(x, "is odd")

# 5
def prn_odd_even(L:list)->None:
    if type(L) != list:
        raise TypeError
    for x in L:
        if type(x) != int:
            raise TypeError
        if x % 2 == 0:
            print(x, "is even")
        else:
            print(x, "is odd")

####################################################
#1 
import sys 
def file_copy(src_file_path:str, dest_file_path:str)->None:
    try:
        f_src = open(src_file_path, "r")
    except FileNotFoundError:
        print("Source file does not exist")
        sys.exit(-1) 
    except PermissionError:
        print("Permission denied to read source file")
        sys.exit(-1)

    try:
        f_dest = open(dest_file_path, "w")
    except FileNotFoundError:
        print("Destination file does not exist")
        sys.exit(-1)
    except PermissionError:
        print("Destination file could not created")
        sys.exit(-1)

    for line in f_src:
        print(line, file = f_dest, end='')

    f_src.close()
    f_dest.close()

    
#2
import sys

def file_copy(src_file_path:str, dest_file_path:str)->None:
    try:
        f_src = open(src_file_path, "r")
    except FileNotFoundError:
        print("Invalid path for source file")
        sys.exit(-1)
    except PermissionError:
        print("Source file cannot be read")
        sys.exit(-1)

    try:
        f_dest = open(dest_file_path, "w")
    except FileNotFoundError:
        print("Invalid path for destination file")
        sys.exit(-1)
    except PermissionError:
        print("Destination file could not created")
        sys.exit(-1)

    for line in f_src:
        print(line, file=f_dest, end='')

    f_src.close()
    f_dest.close()

# 3
import sys

def file_copy(src_file_path:str, dest_file_path:str)->None:
    try:
        f_src = open(src_file_path, "r")
    except FileNotFoundError:
        print("Source file could not be located")
        sys.exit(-1)
    except PermissionError:
        print("Source file could not be read")
        sys.exit(-1)

    try:
        f_dest = open(dest_file_path, "w")
    except FileNotFoundError:
        print("Destination file could not be located")
        sys.exit(-1)
    except PermissionError:
        print("Error in opening destination file in write mode")
        sys.exit(-1)

    for line in f_src:
        print(line, file=f_dest, end='')

    f_src.close()
    f_dest.close()

# 4
import sys

def file_copy(src_file_path:str, dest_file_path:str)->None:
    try:
        f_src = open(src_file_path, "r")
    except FileNotFoundError:
        print("Source file could not be located")
        sys.exit(-1)
    except PermissionError:
        print("Source file does not have read permission")
        sys.exit(-1)

    try:
        f_dest= open(dest_file_path, "w")
    except FileNotFoundError:
        print("Destination file could not be located")
        sys.exit(-1)
    except PermissionError:
        print("Destination file could not be created")
        sys.exit(-1)

    for line in f_src:
        print(line, file=f_dest, end='')

    f_src.close()
    f_dest.close()

# 5
import sys

def file_copy(src_file_path:str, dest_file_path:str)->None:
    try:
        f_src = open(src_file_path, "r")
    except FileNotFoundError:
        print("Could not locate the source file")
        sys.exit(-1)
    except PermissionError:
        print("Could open source file in read mode")
        sys.exit(-1)

    try:
        f_dest = open(dest_file_path, "w")
    except FileNotFoundError:
        print("Could not locate the destionation file")
        sys.exit(-1)
    except PermissionError:
        print("Could not create the destination file")
        sys.exit(-1)

    for line in f_src:
        print(line, file = f_dest, end='')

    f_src.close()
    f_dest.close()