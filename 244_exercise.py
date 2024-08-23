"""
# Let abc.txt be a file in current directory 

# capitalized 

for line in capitalized(f_path): 
    print(line) 

"""

class capitalize_iterator: 
    def __init__(self, G): 
        self.G = G 
    def __next__(self): 
        return self.G.__next__()

class capitalize: 
    def __init__(self, f_path:str): 
        if type(f_path) != str: 
            raise TypeError("Path name must be a string ")

        try: 
            f_handle = open(f_path, "r")
        except FileNotFoundError as e: 
            print(e) 
            raise 
        except PermissionError as e: 
            print(e) 
            raise 
        f_handle.close() 
        self.f_path = f_path

    def __iter__(self):
        def get_generator(f_path:str): 
            for line in open(f_path): 
                line = line.rstrip()
                yield line.upper() 
        return capitalize_iterator(get_generator(self.f_path))
            
for line in capitalize("Gensquare_1.py"): 
    print(line)