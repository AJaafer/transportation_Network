import socket
import sys

# Create an AF_INET (IPv4), STREAM (TCP) socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created.')
# Get the local machine name and assign an arbitrary non-privileged port number
host, port = socket.gethostbyname(socket.gethostname()), 1234
print(str(host) + ' ' +str(port))
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
    try:
        httpRequest=clientsocket.recv(200).decode()
        filename = httpRequest.split(' ')[1]
        sendback1 = 'HTTP/1.1'
        fd = open(filename[1:])
        sendback3 = fd.read()
        fd.close()
        sendback2 = '200 OK'
        result = sendback1 + ' ' + sendback2+ '\r\n\r\n' + sendback3
    except IOError:
        sendback2 = '404 Not Found'
        sendback3 = 'File not here!'
        result = sendback3
    clientsocket.send(result.encode())
    clientsocket.close()
