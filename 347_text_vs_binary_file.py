import sys 
import os 

def main(): 
    text_file_name = "obj.txt"
    binary_file_name = "obj.bin"
    n = 5100
    try: 
        text_file_handle = open(text_file_name, "w")
        binary_file_handle = open(binary_file_name, "wb")
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data)
        sys.exit(-1)
    
    print(n, file=text_file_handle)
    wb = os.write(binary_file_handle.fileno(), b'5100')    
    print(wb)

    text_file_handle.close() 
    binary_file_handle.close() 

main()