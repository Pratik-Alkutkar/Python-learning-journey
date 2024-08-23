class Node: 
    def __init__(self, new_data:int): 
        self.data = new_data 
        self.prev = None 
        self.next = None 

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

    def insert_start(self, new_data): 
        pass 

    def insert_end(self, new_data): 
        pass 
    

def main(): 
    L = linked_list()   
    L.insert_start(100)
    L.insert_end(200)


main()