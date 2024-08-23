import sys 
import dbm 

def main(): 
    dbm_file_path = "storage.bin"
    dbm_handle = dbm.open(dbm_file_path, 'c')
    D = {25 : 'Rohit', 49 : 'Pratik', 58 : 'Suresh'}
    for key in D.keys(): 
        dbm_handle[str(key)] = D[key]
    print('Number of records in storage.bin:', len(dbm_handle))
    dbm_handle.close() 
    sys.exit(0)
    
main() 