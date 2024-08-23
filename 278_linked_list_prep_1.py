# Node with a single link (forward link)

class Node: 
    def __init__(self, new_data:int): 
        if type(new_data) != int: 
            raise TypeError("data must be an integer")
        self.data = new_data 
        self.next = None 

def main(): 
    N1 = Node(100)
    N2 = Node(200)
    print("id(N1):{}, id(N2):{}".format(hex(id(N1)), hex(id(N2))))
    print("N1.__dict__:", N1.__dict__)
    print("N2.__dict__:", N2.__dict__)
    N1.next = N2 
    print("N1.__dict__:", N1.__dict__)
    print("N2.__dict__:", N2.__dict__)
    N3 = Node(300)
    N4 = Node(400)
    print("id(N3):{}, id(N4):{}".format(hex(id(N3)), hex(id(N4))))
    N2.next = N3 
    N3.next = N4 

    print("N1.__dict__:", N1.__dict__)
    print("N2.__dict__:", N2.__dict__)
    print("N3.__dict__:", N3.__dict__)
    print("N4.__dict__:", N4.__dict__)

    N4.next = N1 # This will make a list circular. 
    
    
    print("N1.__dict__:", N1.__dict__)
    print("N2.__dict__:", N2.__dict__)
    print("N3.__dict__:", N3.__dict__)
    print("N4.__dict__:", N4.__dict__)


main()