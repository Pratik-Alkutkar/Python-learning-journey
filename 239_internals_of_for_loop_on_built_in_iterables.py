L = [100, 200, 300, 400]

print("Iteraing on L using for loop")
for x in L: 
    print(x)

print("Iterating on L using internal statements that are run while iterating using for loop")

I = L.__iter__()
print("type(I):", type(I)) # this statement is not run, we are putting it for understanding
                            # <class 'list_iterator'>  
while True: 
    try: 
        n = I.__next__() 
        print(n) 
    except StopIteration: 
        break 