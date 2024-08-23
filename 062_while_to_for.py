import sys 

N = int(input("Enter positive integer"))
if N <= 0: 
    sys.exit(-1)

# print all between 0 to N-1
print("print all between 0 to N-1")
print("Using while")
i = 0 
while i < N: 
    print(i) 
    i = i + 1 

print("Using for")
for i in range(N): 
    print(i)

print("print all between 0 to N ") 
print("using while")
i = 0 
while i <= N: 
    print(i)
    i = i + 1 
print("using for")
for i in range(0, N+1): 
    print(i)

print("Extracting source file paths from command line argument list")
argv = ["ncp.py", "abc.txt", "pqr.txt", "lmn.txt", "uvw.txt", "master.txt"]
argc = len(argv)

i = 1
print("using while") 
while i < argc-1: 
    print(i, argv[i])
    i = i + 1 

print("using for")
for i in range(1, argc-1): 
    print(i, argv[i])
