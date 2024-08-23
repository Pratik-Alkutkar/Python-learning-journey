from socket import * 
import sys 

def main(argc:int, argv:list)->None: 

    server_host = 'localhost'
    server_port = 50007
    nr_max_data = 1024 

    data = b'This is a test line'.split()

    if argc > 1: 
        server_host = argv[1]
        if argc > 2: 
            data = [string.encode() for string in argv[2:]]

    socket_object = socket(AF_INET, SOCK_STREAM)
    socket_object.connect((server_host, server_port))

    for word in data: 
        socket_object.send(word)
        data = socket_object.recv(nr_max_data)
        print("Client Received Data:", data)

    socket_object.close()
    sys.exit(0) 

main(len(sys.argv), sys.argv)
