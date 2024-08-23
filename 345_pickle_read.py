import sys 
import pickle 

def main(): 
    disk_file_path = "mydict.bin"
    disk_file_handle = open(disk_file_path, "rb")
    D = pickle.load(disk_file_handle)
    print(D)
    disk_file_handle.close() 
    sys.exit(0) 

main()