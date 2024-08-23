import sys 

def main():     
    
    m1_str=input("Enter mass of object 1 in kgs:")
    m1=float(m1_str)
    if m1<=0.0: 
        print("Mass cannot be negative")
        sys.exit(-1) 
    
    m2_str=input("Enter mass of object 2 in kgs:")
    m2=float(m2_str)
    if m2<=0.0: 
        print("Mass cannot be negative")
        sys.exit(-1)
    
    r_str=input("Enter the distance between the objects in meters:")  
    r=float(r_str)
    if r<=0.0: 
        print("Distance between the object cannot be zero or negative")
        sys.exit(-1)
    
    G=6.67*(10**-11)
    F=(G*m1*m2)/(r**2)
    print("Gravitational force between two objects is", F, "Newtons")
    
    sys.exit(0)

main()

