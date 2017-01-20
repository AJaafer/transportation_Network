import socket
import sys
# Create an AF_INET (IPv4), STREAM (TCP) socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created.')
# Get the local machine name and assign an arbitrary non-privileged port number
host, port = socket.gethostname(), 1234
try:
    # Bind the socket to the network address
    serversocket.bind((host, port))
except socket.error as msg:
    print('Binding failed. Error code: ' + str(msg[0]) + ', Message: ' + msg[1])
    sys.exit()
print('Binding complete.')
# Queue up to 5 requests
serversocket.listen(5)
print('Socket listening.')
while True:
    # Establish a connection - blocking call
    clientsocket, addr = serversocket.accept()
    print('Connection established.')
    clientsocket.close()
