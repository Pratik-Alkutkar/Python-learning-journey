import sys

def main():
    print("Hello, World!")
    sys.exit(0) 

print(type(main))
print(id(main))
print(sys.getrefcount(main))

main()


