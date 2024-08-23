import sys

def main():
    L = [10, 20, 30, 40]
    i = 0
    while i < len(L):
        print(i, L[i])
        i += 1
    print("END")
    sys.exit(0)

main()