class bst_node: 
    def __init__(self, new_data): 
        self.data = new_data 
        self.left = None 
        self.right = None 
        self.parent = None 

class bst: 
    def __init__(self): 
        self.root_node = None 

    def insert(self, new_data): 
        pass 

    def remove(self, new_data): 
        pass # !!! 

    def prorder(self): 
        pass 

    def postorder(self):
        pass 

    def inorder(self): 
        pass 

    def inorder_successor(self, e_data): 
        pass 

    def inorder_predecessor(self, e_data): 
        pass 

    def max(self): 
        pass 

    def min(self): 
        pass 

def main(): 
    T = bst() 
    for i in range(10): 
        data = random.randint(1, 10000)
        T.insert(data)
    T.prorder() 
    T.inorder() 
    T.postorder() 
    
main()