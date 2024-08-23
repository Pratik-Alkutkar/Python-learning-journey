class ListEmptyError(Exception): 
    pass 

class Node: 
    def __init__(self, new_data:int): 
        self.data = new_data 
        self.prev = None 
        self.next = None 

class linked_list_iterator: 
    def __init__(self, G): 
        self.G = G 

    def __next__(self): 
        return self.G.__next__()

class linked_list: 
    def __init__(self): 
        self.head_node = Node(None)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 

    @staticmethod 
    def generic_insert(beg_node:Node, new_node:Node, end_node:Node) -> None: 
        new_node.next = end_node 
        new_node.prev = beg_node 
        beg_node.next = new_node 
        end_node.prev = new_node 

    @staticmethod 
    def generic_delete(d_node:Node)->Node: 
        d_node.prev.next = d_node.next
        d_node.next.prev = d_node.prev 
        del d_node 

    def insert_start(self, data:int)->bool:
        if type(data) != int: 
            raise TypeError  
        linked_list.generic_insert(self.head_node, Node(data), self.head_node.next)
        return True 
    
    def insert_end(self, data:int)->bool: 
        if type(data) != int: 
            raise TypeError 
        linked_list.generic_insert(self.head_node.prev, Node(data), self.head_node)
        return True 
    
    def insert_after(self, e_data, new_data)->bool: 
        run = self.head_node.next 
        while run != self.head_node: 
            if run.data == e_data: 
                break 
            run = run.next 
        else: 
            raise ValueError("Bad e_data:{}".format(e_data))
        linked_list.generic_insert(run, Node(new_data), run.next)
        return True 

    def insert_before(self, e_data, new_data): 
        run = self.head_node.next 
        while run != self.head_node: 
            if run.data == e_data: 
                break 
            run = run.next 
        else: 
            raise ValueError("Bad e_data:{}".format(e_data))
        linked_list.generic_insert(run.prev, Node(new_data), run)
        return True 

    def remove_start(self)->bool: 
        if self.is_empty() == True:
            raise ListEmptyError("Cannot remove from empty list")
        linked_list.generic_delete(self.head_node.next)
        return True 

    def remove_end(self): 
        if self.is_empty() == True:
            raise ListEmptyError("Cannot remove from empty list")
        linked_list.generic_delete(self.head_node.prev)
        return True 
    
    def remove_data(self, d_data)->bool: 
        run = self.head_node.next 
        while run != self.head_node: 
            if d_data == run.data: 
                break 
            run = run.next 
        else: 
            raise ValueError("Data to be deleted does not exist. {}".format(d_data))
        linked_list.generic_delete(run)
        return True 
        
    def is_empty(self)->bool: 
        return (self.head_node.next == self.head_node and 
                self.head_node.prev == self.head_node)

    def show(self): 
        print("[START]<->", end='')
        run = self.head_node.next 
        while run != self.head_node: 
            print("[{}]<->".format(run.data), end='')
            run = run.next 
        print("[END]")

    def __add__(self, other): 
        # Return a new linked list which is a 
        # concantenated version of self and other 
        # self and other do not undergo any change
        new_list = linked_list() 
        for x in self: 
            new_list.insert_end(x)
        for x in other: 
            new_list.insert_end(x)
        return new_list 

    def __iter__(self): 
        def get_generator(L): 
            run = L.head_node.next 
            while run != L.head_node:  
                yield run.data 
                run = run.next 
        return linked_list_iterator(get_generator(self))
    
    def __contains__(self, search_data): 
        run = self.head_node.next 
        while run != self.head_node: 
            if run.data == search_data: 
                return True 
            run = run.next 
        return False 

    def __str__(self): 
        op_str = '[START]<->'
        run = self.head_node.next 
        while run != self.head_node: 
            op_str = op_str + "[{}]<->".format(run.data)
            run = run.next 
        op_str = op_str + "[END]\n"
        return op_str 
    
    __repr__ = __str__ 

def main(): 
    L = linked_list()   
    L.show() # [START]<->[END]
    print("L:", L) # L:[START]<->[END]
    L.insert_end(10)
    L.insert_end(20)
    L.insert_end(30)
    L.insert_end(40)
    L.show() # 10, 20, 30, 40
    print("L:", L) # L:[START]<->[10]<->[20]<->[30]<->[40]<->[END]
    L.insert_start(8)
    L.insert_start(5)
    L.insert_start(1) # 1, 5, 8, 10, 20, 30, 40
    L.show()
    print("L:", L) 

    print("Iterating over list using iterator pattern")
    for x in L: 
        print(x)

    if not L.is_empty(): 
        print("L is NOT empty")

    # 1, 5, 8, 10, 20, 30, 40
    try: 
        L.insert_after(-100, 100) 
    except ValueError as e: 
        print(e)

    try: 
        L.insert_before(4500, 100) 
    except ValueError as e: 
        print(e)

    if 20 in L: 
        print("20 is a member of list:{}".format(L))

    if not -100 in L: 
        print("-100 is not a member of {}".format(L))

    L.insert_after(10, 100)
    L.insert_before(10, 200)
     # 1, 5, 8, 200, 10, 100, 20, 30, 40
    print("L after insert_after() and insert_before():", L)

    L.remove_start() 
    print("after remove_start():", L)

    L.remove_end() 
    print("After remove_end():", L)

    L.remove_data(10) 
    print("After L.remove(data(10)):", L)

    L1 = linked_list() 
    if L1.is_empty(): 
        print("L1 is empty")
    print("iterating over empty list start")
    for x in L1: 
        print(x) 
    print("iterating over empty list end")

    try:
        L1.remove_start() 
    except ListEmptyError as e: 
        print(e) 

    try: 
        L1.remove_end() 
    except ListEmptyError as e: 
        print(e) 

    print("Interlist functions")
    L1 = linked_list() 
    L2 = linked_list()

    for data in range(5): 
        L1.insert_end(data * 100)
        L2.insert_start((data + 1) * 1000)

    L3 = L1 + L2 
    print("L1:", L1)
    print("L2:", L2)
    print("L3:", L3)

main()

"""
[START]<->[10]<->[20]<->[30]<->[40]<->[END]

>>>L 
"""