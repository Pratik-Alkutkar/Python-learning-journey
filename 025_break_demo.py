import sys

def main():
    L = []
    while True:
        choice = input("Do you want to enter another integer?:[Y-Yes|N-No]:")
        if choice != 'Y' and choice != 'y' and choice != 'Yes' and choice != 'yes':
            break
        n = int(input("Enter an integer:"))
        L.append(n)

    print("Integers entered by user:")
    for x in L:
        print(x) 

    sys.exit(0)

main()