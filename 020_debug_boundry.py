import sys 
print("start")
N = int(input("Enter N:"))
if N < 0:
    print('Error')
    sys.exit(-1)
i = 0
while i <= N:
    print("Repeat #%d" % i)
    i = i + 1
print("end")
