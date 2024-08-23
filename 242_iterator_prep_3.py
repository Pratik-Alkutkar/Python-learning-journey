class MyType: 
    def __iter__(self): 
        print("In __iter__") 


def main(): 
    mt = MyType() 
    for x in mt: 
        print(x) 

main()