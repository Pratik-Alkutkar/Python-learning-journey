from socket import * 
import signal 
import sys 
import time 

def sigint_handler(signum, sigtrace): 
    print("Shutting down the echoserver", end='')
    for i in range(5): 
        print('.', end='', flush=True)
        time.sleep(1) 
    print("\nServer has shut down. Bye!")
    sys.exit(0)

def main(): 

    signal.signal(signal.SIGINT, sigint_handler)

    host_name = 'localhost'
    port_number = 50007 
    nr_max_pending_connects = 5 
    nr_max_recv_bytes = 1024 

    socket_object = socket(AF_INET, SOCK_STREAM)
    socket_object.bind((host_name, port_number))
    socket_object.listen(nr_max_pending_connects)
    while True: 
        print("Waiting for the next client:")
        (connection, address) = socket_object.accept()
        print("Receiving Data From:", address)
        while True: 
            data = connection.recv(nr_max_recv_bytes)
            if len(data) == 0: 
                break
            connection.send(b'>>>' + data)
        connection.close() 

main()
