"""
@goal:  to illustrate emaining methods of json package 
        (methods covered so far: loads, dumps)
"""

import sys 
import json 

def dump_dict_to_json_file(json_file_path:str)->None: 
    info_dict = {
        "b1" : True, 
        "b2" : False, 
        "n_int" : 345, 
        "f_float" : 2.14, 
        "T" : (1, 2, 3), 
        "L" : [100, 200, 300, 400], 
        "s" : "This is a string", 
        "None" : None
    }

    try: 
        json_handle = open(json_file_path, "w")
    except: 
        exc_name, exc_data, _ = sys.exc_info() 
        print(exc_name, exc_data)
        sys.exit(-1)

    json.dump(info_dict, json_handle)
    json_handle.close() 


def main(argc:int, argv:list)->None: 
    if argc != 2: 
        print("UsageError:{} json_file_path".format(argv[0]))
        sys.exit(-1)

    with open(argv[1], "r") as json_handle: 
        json_dict = json.load(json_handle)

    for(key, val) in json_dict.items():
        print(key, val, type(key), type(val), sep=':')

    dump_dict_to_json_file("py_to_json.json")

    sys.exit(0) 

main(len(sys.argv), sys.argv)