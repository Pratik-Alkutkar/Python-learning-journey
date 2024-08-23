import sys 

def main():
    line = "-" * 65
    print(line)
    
    print("find")
    s = "aaBBaaBBBaaBBB"
    print("s.find('aa'):", s.find('aa'))

    n = s.find("BCD")
    print("n:", n)
    print(line)
    
    # strip, rstrip, lstrip 
    s = "\n\n\tHello\n\n"
    s1 = s.strip()
    print("s1:", s1)

    s2 = s.rstrip()
    print("s2:", s2)

    s3 = s.lstrip() 
    print("s3:", s3)
    print(line)
    
    # split, rsplit, splitlines, join  
    s = "pratik:x:1001:1001:Pratik Alkutkar,,,:/home/pratik:/bin/bash"
    L = s.split(":")
    print("split:L:", L)

    L = s.split(":", maxsplit=3)
    print("split with maxsplit:L:", L)
    
    L = s.rsplit(":", maxsplit=3)
    print("rsplit:L:", L)

    s = "Hello\nPython\nWorld"
    L = s.splitlines()
    print("s.splitlines():", L)

    delim = "##"
    s_joined = delim.join(L)
    print("s_joined:", s_joined) 
    print(line)
    
    # partition, rpartition 
    s = "Processor - Corei7 6950x"
    T = s.partition("-")
    print("First:", T[0])
    print("Sep:", T[1])
    print("Second:", T[2])

    T = s.rpartition("-")
    print("Second:", T[0])
    print("Sep:", T[1])
    print("First:", T[2])
    print(line)
    
    # format, format_map 
    s = "My name is {} My number is {}"
    sf = s.format("Yogeshwar", 9561547043)
    print("sf:", sf)

    M = {"flag" : True, "delete" : False}
    s = "Condition {flag} Operation {delete}"
    sf = s.format_map(M)
    print("sf:", sf)
    print(line)
    
    # replace 
    s = "Hello,World,Python"
    sr = s.replace(",", "##")
    print("sr:", sr)
    print(line)
    
    # upper, lower, title, swapcase, casefold, capitalize 
    s_lower = "helloworld"
    s_upper = "HELLOWORLD"

    s1 = s_lower.upper()
    s2 = s_upper.lower() 

    print("s_lower.upper():", s1, "s_upper.lower():", s2) 

    s = "hello python world"
    s_title = s.title() 
    print("s_title:", s_title)

    s = "Hello Python World"
    s1 = s.swapcase()
    print("s:", s, "s.swapcase():", s1)

    s2 = s.casefold()
    print("s:", s, "s.casefold():", s2)

    s = "this is a good city."
    s1 = s.capitalize()
    print("s.capitalize():", s1)
    print(line)
    
    # ljust, rjust, center 
    # len(s) = 18 
    s = "Hello Python World"
    s_ljust = s.ljust(22)
    print("s.ljust():", s_ljust, "end")

    s_rjust = s.rjust(22)
    print("s.rjust():", s_rjust)

    s_center = s.center(22)
    print("s.center(22):", s_center, "end")
    print(line)
    
    # startswith, endswith 
    s = "12_2020-LOGS"
    b = s.startswith("12")
    print("s:", s, "s.startswith('12'):", b)

    s = "HelloWorld.cpp"
    b = s.endswith(".cpp")
    print("s:", s, "s.endswith('.cpp'):", b) 
    print(line)
    
    # isalnum, isalpha, isascii, isdigit, isidentifier, 
    # islower, isprintable, isspace, istitle, isupper 
    s = "abc123"
    print("isalnum:", s.isalnum())
    s = "ABCD"
    print("isalpha:", s.isalpha())
    s = "ABC123%&^^&"
    print("isascii:", s.isascii())
    s = "3453536"
    print("isdigit:", s.isdigit())
    s = "f_num"
    print("isidentifier:", s.isidentifier()) 
    s = "abcefg"
    print("islower:", s.islower())
    s = "ABCEFG"
    print("isupper:", s.isupper())
    s = "jsafksaf&(*&(*&9asfjkasf"
    print("isprintable:", s.isprintable())
    s = "\t     \n    \t"
    print("isspace:", s.isspace())
    s = "Hello Python World"
    print("istitle:", s.istitle())

    print(line)
    
    # Misc : encode, expandtabs, zfill  
    s = "HelloWorld"
    sb = s.encode()
    print("encode:type(sb):", type(sb))

    s = "Hello\tWorld"
    print("expandtabs:s:", s)
    print("expandtabs:len(s):", len(s))

    st = s.expandtabs()
    print("expandtabs:st:", st)    
    print("expandtabs:len(st):", len(st))

    s = "Hello"
    sz = s.zfill(10)
    print("zfill:sz:", sz)

    print(line)
    sys.exit(0) 

main()