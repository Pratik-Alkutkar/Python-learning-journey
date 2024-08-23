import dbm 
import sys 

def main(): 
    dbm_file_path = "storage.bin"
    dbm_handle = dbm.open(dbm_file_path, 'c')
    for key in dbm_handle: 
        print(key.decode(), dbm_handle[key].decode())
    dbm_handle.close()   
    sys.exit(0)  

main() 