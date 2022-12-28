import socket
import sys
import threading
def run_client(id):
    # Create a TCP/IP socket 
    client = socket.socket()
    # Define host 
    host = '127.0.0.1'
    # define the communication port 
    port = id+1024
    # Connect the socket to the port where the server is listening 
    server_address = ((host, port))
    print("connecting")
    client.connect(server_address)
    # Send data 
    while True:
        try:
            x = input('> ')
            if "" != x:
                print("Send: ", x)
                client.send(x.encode('utf-8'))
                if "DONE" == x:
                    print("shutting down")
                    break
        except KeyboardInterrupt as k:
            print("shutting down")
            break

    client.close()

# start_client()