import sys 
import os 

def main(): 
    cwd_path = os.getcwd()
    print(cwd_path) 
    new_dir_path = os.path.join(cwd_path, "TEST_DIR")
    print("New dir path:", new_dir_path)
    os.makedirs(new_dir_path)
    os.chdir(new_dir_path)
    cwd_path = os.getcwd()
    print(cwd_path) 
    f_handle = open("abc.txt", "w")
    f_handle.close() 
    f_handle = open("pqr.txt", "w")
    f_handle.close() 
    f_handle = open("lmn.txt", "w")
    f_handle.close() 
    print("Files in {}".format(new_dir_path))
    for f_name in os.listdir(new_dir_path): 
        print(f_name)

main() 

"""
getcwd() 
os.path.join() 
os.mkdirs()
os.listdir()
"""