import sys 

def main(): 
    
    # Ways of creation 
    # Singly quoted string" 
    s1 = 'This is a singly quoted string' 
    s2 = 'Singly quoted stirng can contain " as a data' 
    print("s1:", s1, "type(s1):", type(s1)) 
    print("s2:", s2, "type(s2):", type(s2)) 

    # Doubly quoted string 
    s3 = "This is a doubly quoted string" 
    s4 = "Doubly quoted string can contain ' as a data" 
    print("s3:", s3, "type(s3):", type(s3)) 
    print("s4:", s4, "type(s4):", type(s4)) 

    # Escape sequences : Work with both singly and doubly quoted strings  
    s5 = "Hello\tWorld" 
    s6 = 'Hello\nWorld' 
    print("s5:", s5)
    print("s6:", s6) 

    # Raw strings 
    s7 = r"Hello\nWorld"
    path = r"C:\New Folder\abc.txt" 
    print("s7:", s7)
    print("path:", path) 

    # Triple quoted string 
    s8 = """This is a triple quoted stirng 
            it can contain new line without
            having to use an escape sequence 
            therefore can span across multiple 
            lines. It can contain ' and " as data 
            simultaneously and ends only with 
            matching triple quotes 
        """ 
    print("s8:", s8) 

    s9 = '''Triple quoted strings are used as 
            comments as well as as docstrings 
            concepts that shall be illustrated
            in the class
        '''
    print("s9:", s9) 

    # Creating string from bool, integer, float 
    b = True
    n = 10
    f = 3.14
    print("b:", b, "type(b):", type(b))
    print("n:", n, "type(n):", type(n))
    print("f:", f, "type(f):", type(f)) 
    s1 = str(b)
    s2 = str(n)
    s3 = str(f)
    print("s1:", s1, "type(s1):", type(s1)) 
    print("s2:", s2, "type(s2):", type(s2)) 
    print("s3:", s3, "type(s3):", type(s3)) 

    # Built-in functions 
    s = "Hello,World!" 
    print("s:", s)
    print("type(s):", type(s))
    print("len(s):", len(s))
    print("id(s):", id(s)) 

    # Built in operators on string 
    # Concatenation (s1 + s2) 
    s1 = "Hello" 
    s2 = "World" 
    s3 = s1 + s2
    s4 = s1 + "," + s2 + "!" 
    print("s3:", s3)
    print("s4:", s4) 

    # Multiplication by scalar (s * n)
    s1 = "Hey!" 
    s2 = s1 * 3
    print("s2:", s2) 

    # Index (s[i]) 
    s = "Hello!"
    print("s[0]:", s[0])
    print("s[2]:", s[2])

    # Traversing through string indexwise 
    for i in range(len(s)):
        print("s[", i, "]:", s[i]) 

    # Negative indexing 
    print("s[-1]:", s[-1])
    print("s[-3]:", s[-3]) 

    # Range operation (s[i:j]) 
    s = "This is a long string created for the purpose of illustration" 
    print("len(s):", len(s)) # len(s) = 61 
    print("s[3:7]:", s[3:7])
    print("s[1:10]:", s[1:10])
    print("s[3:40]:", s[3:40]) 
    
    # Range operation with negative indices 
    print("s[-40 : -20]:", s[-40:-20]) 
    print("s[-17:-1]:", s[-17:-1]) 

    # Range operation with anchor character 
    print("s[ : 10]=", s[:10])
    print("s[40 : ]=", s[40 : ]) 

    # Slice operation s[i : j : k] 
    # with positive k 
    print("s[1 : 10 : 3]:", s[1 : 10 : 3])
    print("s[3 : 25 : 4]:", s[3 : 25 : 4]) 

    # With anchor syntax 
    print("s[ : 10 : 2]:", s[ : 10 : 2])
    print("s[ : 20 : 4]:", s[ : 20 : 4])
    print("s[30 : : 3]:", s[ : 30 : 3]) 
    print("s[: : 2]:", s[: : 2]) 

    # with negative k 
    print("s[7 : 1 : -2]:", s[7 : 1 : -2]) 
    print("s[8 : 2 : -1]:", s[8 : 2 : -1]) 
    print("s[::-1]:", s[::-1]) 

    # Rules: 
    # k > 0 and i < j => len(s[i : j : k]) > 0 
    # k > 0 and i >= j => len(s[i : j : k) = 0 
    # k < 0 and i > j => len(s[i : j : k]) > 0 
    # k < 0 and i <= j => len(s[i : j : k]) = 0 
    # len(s[i : j : k]) > 0 => (k > 0 and i < j) or
    #                          (k < 0 and i > j) 
    # len(s[i : j : k]) = 0 => (k > 0 and i >= j) or 
    #                           (k < 0 and i <= j) 
    # s[-i] = s[len(s) - i]

    # Useful Patterns 
    # First k chars     :   s[: k] 
    # From k to last    :   s[k : ]
    # Last k characters :   s[-k : ] 
    # Reversed s[i:j]   :   s[j-1 : i - 1 : -1] 
    # Reversed string   :   s[: : -1]
    # All even indices  :   s[: : 2]
    # All odd indices   :   s[1 : : 2] 

    # String : class methods 
    # index
    s = "aaBBaaBBBaaCCCCaaDDD" 
    n1 = s.index("aa")
    print("n:", n)
    n2 = s.index("aa", n1+1)
    print("n2:", n2) 
    n3 = s.index("aa", n2+1)
    print("n3:", n3) 
    n4 = s.index("aa", n3 + 1)
    print("n4:", n4) 

    # count method 
    print("Count method")
    n = s.count("aa")
    print("n:", n) 

    n = s.count("CCCC")
    print("n:", n)

    n = s.count("XYZ")
    print("n:", n)

main() 
