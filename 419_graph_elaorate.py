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
    def __init__(self, v, w=0.0): 
        self.v = v 
        self.weight = w 
        self.prev = None 
        self.next = None 

class hlist: 
    
    class hlist_iterator: 
        def __init__(self, G): 
            self.G = G 
        def __next__(self): 
            return next(self.G)
    
    def __init__(self): 
        self.head_node = hnode(None)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 

    def insert_end(self, v): 
        common_list_methods.generic_insert(self.head_node, hnode(v))

    def __iter__(self): 
        def build_generator(head_node): 
            run = head_node.next 
            while run != head_node: 
                yield (run.v, run.weight)
                run = run.next
        return hlist.hlist_iterator(build_generator(self.head_node))

class node_color: 
    WHITE = 0 
    GRAY = 1 
    BLACK = 2 

class vnode: 
        
    def __init__(self, v, color = node_color.WHITE):
        self.v = v
        self.color = color
        self.hlist = hnode(None)
        self.hlist.prev = self.hlist
        self.hlist.next = self.hlist 
        self.prev = None 
        self.next = None 

class vlist: 

    class vlist_iterator: 
        def __init__(self, G): 
            self.G = G 
        def __next__(self): 
            return next(self.G)

    def __init__(self): 
        self.head_node = vnode(None)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 
        del self.head_node.hlist 
        del self.head_node.color 

    def insert_end(self, new_v): 
        common_list_methods.insert_end(self.head_node, vnode(new_v))

    def __iter__(self): 
        def build_generator(head_node): 
            run = head_node.next 
            while run != head_node: 
                yield (run.v, run.color, run.hlist)
                run = run.next 
        return vlist.vlist_iterator(build_generator(self.head_node))

class edge_node: 
    def __init__(self, v_start, v_end, w=0): 
        self.v_start = v_start 
        self.v_end = v_end 
        self.weight = w 
        self.prev = None 
        self.next = None

class edge_list: 

    class edge_list_iterator: 
        def __init__(self, G): 
            self.G = G 
        def __next__(self): 
            return next(self.G)

    def __init__(self): 
        self.head_node = edge_node(None, None)
        self.head_node.prev = self.head_node 
        self.head_node.next = self.head_node 
    
    def insert_end(self, start_vertex, end_vertex): 
        for (start_v, end_v, _) in self: 
            if (start_v == start_vertex and end_v == end_vertex) or (start_v == end_vertex and end_v == start_vertex): 
                raise ValueError("Edge exists")
        common_list_methods.insert_end(self.head_node, edge_node(start_vertex, end_vertex))

    def __iter__(self): 
        def build_generator(head_node): 
            run = head_node.next 
            while run != head_node: 
                yield (run.v_start, run.v_end, run.weight) 
                run = run.next 
        return edge_list.edge_list_iterator(self.head_node)

class graph: 
    def __init__(self): 
        self.V = vlist(None)
        self.E = edge_list(None)
        self.nr_vertices = 0 
        self.nr_edges = 0 
        
def main(): 
    g = graph() 
    # v = (v, color, hlist)
    # h = (vertex, weight)
    # e = (start_vertex, end_vertex, weight)

    for (vertex, color, hlist) in g.V: 
        print("do something with v")
        for (vertex, weight) in hlist: 
            print("do something with h")

    for (start_vertex, end_vertex, weight) in g.E: 
        print("do something with e")

main()

"""
TODO : 
1] add_vertex() in graph 
2] remove_vertex() in graph 
3] add_edge() in graph 
4] add_vertex() in graph 
-------------------------------------
5] dfs() in graph 
6] bfs() in graph 
7] dijikstra() in graph     -> GREEDY 
8] bellman_ford() in graph  -> GREEDY 
9] prims() in graph         -> GREEDY 
10] kruskal() in graph      -> GREEDY 
--------------------------------------
ADVANCED TREES 
NETWORK 
DYNAMIC PROGRAMMING
-------------------------------------- 
BACKTRACKING 
BRANCH-AND-BOUND 
--------------------------------------
DESIGN PATTERN
--------------------------------------
PYTHON-C
---------------------------------------
24LPA
"""