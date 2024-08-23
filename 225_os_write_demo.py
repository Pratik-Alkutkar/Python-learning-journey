import sys, os 

def main(): 
    name = "Pratik"
    roll = 1 
    s = "My Name is {} My Roll Number is {}".format(name, roll)
    print(type(s)) # str object 
    sb = s.encode() # byte object containing C like char array 
    os.write(1, sb)
    sys.exit(0) 

main() 

# f_handle = open("abc.txt", "r")

# _io.TextIOWrapper

# os.open()