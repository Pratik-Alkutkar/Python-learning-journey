"""
Create a class to capture a node in horizontal list 
Create a class to capture a node in vertical list 
Write a constructor of graph in terms of them. 

and then add methods! 
"""

class common_list_methods: 
    @staticmethod 
    def generic_insert(start_node, mid_node, end_node): 
        mid_node.next = end_node
        mid_node.prev = start_node 
        start_node.next = mid_node 
        end_node.prev = mid_node 

    @staticmethod 
    def generic_delete(delete_node): 
        delete_node.prev.next = delete_node.next 
        delete_node.next.prev = delete_node.prev 

    @staticmethod 
    def search_node(head_node, data): 
        run = head_node.next 
        while run != head_node: 
            if run.v == data: 
                return run 
            run = run.next 
        return None 

    @staticmethod 
    def insert_end(head_node, new_node): 
        common_list_methods.generic_insert(head_node.prev, new_node, head_node)

class hnode: 
    def __init__(self, v): 
        self.v = v 
        self.prev = None 
        self.next = None 

    def insert_end(self, v): 
        common_list_methods.insert_end(self.head_node, hnode(v))

class vnode: 
    def __init__(self, v): 
        self.v = v 
        self.prev = None 
        self.next = None 
        self.hlist = hnode(None) 
        self.hlist.prev = self.hlist 
        self.hlist.next = self.hlist 

    def insert_end(self, v): 
        common_list_methods.insert_end(self.head_node, vnode(v))

class graph: 
    def __init__(self): 
        self.vlist = vnode(None)
        self.vlist.prev = self.vlist
        self.vlist.next = self.vlist
        del self.vlist.hlist  

    def add_vertex(self, new_v): 
        v_node = common_list_methods.search_node(self.vlist, new_v)
        if v_node is not None: 
            raise ValueError("Vertex exists.")
        common_list_methods.insert_end(self.vlist, vnode(new_v))

    def add_edge(self, start_vertex, end_vertex): 
        v_start = common_list_methods.search_node(self.vlist, start_vertex)
        if v_start is None: 
            raise ValueError("Non-existent vertex")
        
        v_end = common_list_methods.search_node(self.vlist, end_vertex)
        if v_end is None: 
            raise ValueError("Non-existent vertex")
        
        h_start = common_list_methods.search_node(v_start.hlist, end_vertex)
        if h_start is not None: 
            raise ValueError("Edge exists.")
        
        h_end = common_list_methods.search_node(v_end.hlist, start_vertex)
        if h_end is not None: 
            raise ValueError("Graph is coprrupted")

        common_list_methods.insert_end(v_start.hlist, hnode(end_vertex))
        common_list_methods.insert_end(v_end.hlist, hnode(start_vertex))

    def remove_vertex(self, v): 
        v_delete = common_list_methods.search_node(self.vlist, v)
        if v_delete is None: 
            raise ValueError("Nonexistent vertex") 
        h_in_v = None
        run_h = v_delete.hlist.next 
        run_h_next = None 
        while run_h != v_delete.hlist: 
            run_h_next = run_h.next 
            h_in_v = common_list_methods.search_node(self.vlist, run_h.v)
            N = common_list_methods.search_node(h_in_v.hlist, v)
            common_list_methods.generic_delete(N)
            common_list_methods.generic_delete(run_h)
            run_h = run_h_next
        common_list_methods.generic_delete(v_delete)

    def remove_edge(self, start_vertex, end_vertex): 
        v_start = common_list_methods.search_node(self.vlist, start_vertex)
        if v_start is None: 
            raise ValueError("Nonexistent vertex")
        v_end = common_list_methods.search_node(self.vlist, end_vertex)
        if v_end is None: 
            raise ValueError("Nonexistent vertex")
        h_end_in_start = common_list_methods.search_node(v_start.hlist, end_vertex)
        if h_end_in_start is None: 
            raise ValueError("Nonexistent edge")
        h_start_in_end = common_list_methods.search_node(v_end.hlist, start_vertex)
        if h_start_in_end is None: 
            raise ValueError("Nonexistent edge")
        common_list_methods.generic_delete(h_start_in_end)
        common_list_methods.generic_delete(h_end_in_start)
        
    def __str__(self): 
        display_string = "\n"
        run_v = self.vlist.next 
        while run_v != self.vlist: 
            display_string += "[{}]\t->\t".format(run_v.v) 
            run_h = run_v.hlist.next 
            while run_h != run_v.hlist: 
                display_string += "[{}]<->".format(run_h.v)
                run_h = run_h.next 
            display_string += "[END]\n"
            run_v = run_v.next 
        display_string += '\n'
        return display_string

def main(): 
    g = graph() 
    V = (1, 2, 3, 4, 5, 6)
    E = [(1, 2), (1, 6), (2, 5), (2, 4), (3, 6), (3, 5), (3, 4), (5, 1), (6, 2)]

    for vertex in V: 
        g.add_vertex(vertex)
    
    for edge in E: 
        g.add_edge(edge[0], edge[1])

    print("Initial state:", g)
        
    g.add_vertex(7)
    g.add_edge(7, 1)
    g.add_edge(7, 5)
    g.add_edge(7, 3)

    print("After adding vertex(7) and edges-(7,1), (7,5), (7, 3):", g)
    
    g.remove_edge(1, 6)
    g.remove_edge(2, 4)
    
    print("After removal of edges-(1, 6), (2, 4):", g)

    g.remove_vertex(2) 
    g.remove_vertex(6) 

    print("After removal of two vertices-2, 6:", g)
    
    """
    # Refer Introduction to Algorithm 3rd Edition by 
    # Cormen, Rivest, Leiserson to find accurate pseudocodes 
    # of DFS and BFS. 
    # Implement those algorithms in class graph and test the output 
    v = 2
    g.dfs(v)
    v = 5
    g.bfs(v)
    del g 
    """

main()
