class Date:
    def __init__(self):
        self.day = 26
        self.month = 1
        self.year = 2023

def main():
    D=Date()
    print(D.__dict__)

    D1 = Date() 
    D2 = Date() 
    D3 = Date()

main() 

