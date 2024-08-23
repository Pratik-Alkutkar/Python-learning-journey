class Node: 
    def __init__(self, new_data): 
        self.data = new_data 
        self.prev = None 
        self.next = None 

def main(): 
    N1 = Node(100)
    N2 = Node(200)
    N3 = Node(300)
    N4 = Node(400)

    N1.next = N2 
    N2.next = N3 
    N3.next = N4 

    N4.prev = N3 
    N3.prev = N2 
    N2.prev = N1 

    print("id(N1):{}, id(N2):{}, id(N3):{}, id(N4):{}".format(hex(id(N1)), 
        hex(id(N2)), hex(id(N3)), hex(id(N4))))
    print("Doubly Linked List")
    print("N1.__dict__:{}".format(N1.__dict__))
    print("N2.__dict__:{}".format(N2.__dict__))
    print("N3.__dict__:{}".format(N3.__dict__))
    print("N4.__dict__:{}".format(N4.__dict__))

    N4.next = N1 
    N1.prev = N4 
    print("Doubly Circular Linked List")
    print("N1.__dict__:{}".format(N1.__dict__))
    print("N2.__dict__:{}".format(N2.__dict__))
    print("N3.__dict__:{}".format(N3.__dict__))
    print("N4.__dict__:{}".format(N4.__dict__))

main()