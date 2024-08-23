import pickle 

class OnDiskObject: 
    def __init__(self, init_object): 
        self.binary_file_path = "tmp.bin" 
        self.binary_file_object = open(self.binary_file_path, "wb")
        pickle.dump(init_object, self.binary_file_object) 
        self.binary_file_object.close() 

    def get_data(self): 
        self.binary_file_object = open(self.binary_file_path, "rb")
        ret = pickle.load(self.binary_file_object) 
        self.binary_file_object.close() 
        return ret 

    def set_data(self, rhs_object): 
        self.binary_file_object = open(self.binary_file_path, "wb")
        pickle.dump(rhs_object, self.binary_file_object) 
        self.binary_file_object.close() 

    def del_data(self): 
        self.binary_file_object = open(self.binary_file_path, "wb")
        self.binary_file_object.close()
    
    data = property(get_data, set_data, del_data)


def main(): 
    ODO = OnDiskObject([10, 20, 30, 40, 50])
    print(ODO.data)
    ODO.data = (-1, -2, -3)
    print(ODO.data)
    del ODO.data

main()