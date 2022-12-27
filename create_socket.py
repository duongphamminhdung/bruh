import socket
import sys
# Create a TCP/IP socket 
sock = socket.socket()
# Define host 
host = 'localhost'
# define the communication port 
port = 8080
# Bind the socket to the port 
sock.bind((host, port))
# Listen for incoming connections 
sock.listen(1)
# Wait for a connection 
print('waiting for a connection')
(connection, client) = sock.accept()
print(client, 'connected')
# Receive the data in small chunks and retransmit it 
while True:
    data = connection.recv(10)
    print('received "%s"' % data)
    if not data:
        break
    else:
        print('-'*20)
        print(data.decode('utf-8'))
        if "DONE" == data.decode('utf-8'):
            break
# Close the connection 
connection.close()