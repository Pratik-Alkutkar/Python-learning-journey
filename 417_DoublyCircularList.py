"""
data 
ref to next data 
ref to prev data 

OBJECT T 
    data 
    ref to prev object of type T (forward link)
    ref to next object of type T (backward link)

self referential class =   a class whose object contains 
                            a reference variable to the 
                            object of its own then the class 
                            is known as self referential class 
[None]  [ 10]   [20 ]   [.  ]   [.  ]   [50 ]
[prev]  [   ]   [   ]   [   ]   [   ]   [   ]
[next]  [   ]   [   ]   [   ]   [   ]   [   ]
"""

class DoublyCircularList: 
    
    class Node: 
        def __init__(self, new_data:any): 
            self.data = new_data
            self.prev = None 
            self.next = None

    class DoublyCircularList_Iterator: 
        def __init__(self, G): 
            self.G = G 
        def __next__(self): 
            return next(self.G)

    @staticmethod 
    def generic_insert(beg_node:Node, mid_node:Node, end_node:Node)->None: 
        mid_node.next = end_node 
        mid_node.prev = beg_node 
        beg_node.next = mid_node
        end_node.prev = mid_node

    @staticmethod 
    def generic_delete(delete_node:Node)->None: 
        delete_node.prev.next = delete_node.next
        delete_node.next.prev = delete_node.prev 

    def search_node(self, search_data:any):
        run = self.head_node.next
        while run != self.head_node: 
            if run.data == search_data: 
                return run 
            run = run.next 
        return None 
    
    def __init__(self): 
        self.head_node = self.Node(None)
        self.head_node.prev = self.head_node
        self.head_node.next = self.head_node 

    def insert_start(self, new_data:any)->bool: 
        self.generic_insert(self.head_node, self.Node(new_data), self.head_node.next)
        return True 

    def insert_end(self, new_data:any)->bool: 
        self.generic_insert(self.head_node.prev, self.Node(new_data), self.head_node)
        return True 

    def insert_after(self, e_data:any, new_data:any)->bool: 
        e_node = self.search_node(e_data)
        if e_node is None: 
            raise ValueError("Bad existing data:{}".format(e_data))
        self.generic_insert(e_node, self.Node(new_data), e_node.next)
        return True 

    def insert_before(self, e_data:any, new_data:any)->bool: 
        e_node = self.search_node(e_data) 
        if e_node is None: 
            raise ValueError("Bad existing data:{}".format(e_data))
        self.generic_insert(e_node.prev, self.Node(new_data), e_node)
        return True 

    def remove_start(self)->bool: 
        if self.is_empty(): 
            raise ValueError("Cannot remove the start of empty list")
        self.generic_delete(self.head_node.next)
        return True 

    def remove_end(self)->bool: 
        if self.is_empty(): 
            raise ValueError("Cannot remove the end of empty list")
        self.generic_delete(self.head_node.prev)

    def remove_data(self, d_data)->bool: 
        e_node = self.search_node(d_data)
        if e_node is None: 
            raise ValueError("Cannot remove non existen data:{}".format(d_data))
        self.generic_delete(e_node) 

    def get_start(self)->any: 
        if self.is_empty(): 
            raise ValueError("Cannot get_start of empty list") 
        return self.head_node.next.data 

    def get_end(self)->any: 
        if self.is_empty(): 
            raise ValueError("Cannot get_end of empty list")
        return self.head_node.prev.data 

    def pop_start(self)->any:
        if self.is_empty(): 
            raise ValueError("Cannot pop_start of empty list") 
        ret_data = self.head_node.next.data 
        self.generic_delete(self.head_node.next)
        return ret_data 
         
    def pop_end(self)->any: 
        if self.is_empty(): 
            raise ValueError("Cannot get_start of empty list") 
        ret_data = self.head_node.prev.data 
        self.generic_delete(self.head_node.prev)
        return ret_data 

    def is_empty(self): 
        return self.head_node.next == self.head_node and self.head_node.prev == self.head_node

    def merge(self, other): 
        merged_list = DoublyCircularList()
        run1 = self.head_node.next 
        run2 = other.head_node.next 
        while True:
            if run1 == self.head_node: 
                while run2 != other.head_node: 
                    merged_list.insert_end(run2.data)
                    run2 = run2.next 
                break 

            if run2 == other.head_node: 
                while run1 != self.head_node: 
                    merged_list.insert_end(run1.data)
                    run1 = run1.next 
                break 
            
            if run1.data <= run2.data: 
                merged_list.insert_end(run1.data)
                run1 = run1.next 
            else: 
                merged_list.insert_end(run2.data)
                run2 = run2.next 
        
        return merged_list

    def __add__(self, other): 
        concatenated_list = DoublyCircularList() 
        for x in self: 
            if 'copy' in type(x).__dict__.keys(): 
                x = x.copy() 
            concatenated_list.insert_end(x)  
        for x in other: 
            if 'copy' in type(x).__dict__.keys(): 
                x = x.copy() 
            concatenated_list.insert_end(x)
        return concatenated_list

    def __mul__(self, repeat_count:int): 
        if repeat_count < 0: 
            raise ValueError("Bad value for multipliand:{}".format(repeat_count))
        if repeat_count == 0: 
            return DoublyCircularList() 
        new_list = DoublyCircularList() 
        for i in range(repeat_count): 
            for x in self: 
                if 'copy' in dir(type(x)): 
                    x = x.copy()
                new_list.insert_end(x)
        return new_list

    def __iter__(self): 
        def build_generator(head_node): 
            run = head_node.next 
            while run != head_node: 
                yield run.data 
                run = run.next 
        return self.DoublyCircularList_Iterator(build_generator(self.head_node)) 

    def __contains__(self, element:any)->bool: 
        e_node = self.search_node(element)
        if e_node is None: 
            return False 
        return True 

    def __str__(self)->str: 
        display_string = "[START]<->" 
        run = self.head_node.next 
        while run != self.head_node: 
            display_string += "[{}]<->".format(run.data)
            run = run.next 
        display_string += "[END]"
        return display_string 

if __name__ == '__main__':
    
    def main(): 
        L = DoublyCircularList() 
        print("empty:", L.is_empty())
        for x in range(1, 6): 
            L.insert_end(x*10)
        print(L)
        for x in range(6, 10): 
            L.insert_start(x*10)
        print(L)
        L.insert_after(10, 100)
        print(L)
        L.insert_before(10, 200)
        print(L)
        x = L.get_start() 
        print("start:", x)
        x = L.get_end() 
        print("end:", x)
        x = L.pop_start() 
        print("start:", x)
        print(L)
        x = L.pop_end() 
        print("end:", x)
        print(L)
        L.remove_start() 
        print(L)
        L.remove_end() 
        print(L)
        L.remove_data(10)
        print(L)
        print("empty:", L.is_empty())

        print("Iterate:")
        for x in L:
            print(x) 

        if 100 in L:
            print("100 in L")

        if not -100 in L:
            print("-100 not in L")

        L1 = DoublyCircularList() 
        L2 = DoublyCircularList() 
        for x in range(5): 
            L1.insert_end((x+1) * 5)
        for x in range(7): 
            L2.insert_end((x+1) * 10)
        L3 = L1  + L2 
        L4 = L1 * 5
        L5 = L1.merge(L2)
        print("L1:", L1) 
        print("L2:", L2)
        print("L3=L1+L2:", L3)
        print("L4=L1*5", L4)
        print("L5=L1.merge(L2):", L5)
    
    main()