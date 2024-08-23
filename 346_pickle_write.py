import sys 
import pickle 

def main(): 
    # Create a complex in memory object 
    D = {
            'a': [(100, 200, 300), {400, 500, 600}],  
            'b': ['Hello', 'Python', 'World'],
            'c': [{'x':-100, 'y':-200}, (-1000, -2000)]
         }
    disk_file_path = "mydict.bin"
    disk_file_handle = open(disk_file_path, "wb")
    # In memory object will be stored on disk file 
    # to be retrieved as dictionary object by reader code 
    pickle.dump(D, disk_file_handle)
    disk_file_handle.close() 

main() 