'''
xingeng wang
11144515
xiw031
'''

import socket
import sys
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES
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
random_generator = Random.new().read
server_key = RSA.generate(1024,random_generator)
server_publickey = server_key.publickey()
while True:
    # Establish a connection - blocking call
    clientsocket, addr = serversocket.accept()
    print('Connection established.')

    clientsocket.send(server_publickey.exportKey())
    symmetricKey = clientsocket.recv(2048)

    decrypt_symmetricKey = server_key.decrypt(symmetricKey)
    aes = AES.new(decrypt_symmetricKey, AES.MODE_ECB)
    cipherText = clientsocket.recv(2048)

    result = aes.decrypt(cipherText).decode()

    print(result)
    clientsocket.close()
