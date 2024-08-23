import sys
print("Start of program") 
N = int(input("Enter number of repetitions::"))
if N < 0:
    print("Number of repetitions should be zero or positive")
    sys.exit(-1)
i=0
while i<N:
    print("Repetition Number %d" % i)
    i=i+1
print("End of program")
