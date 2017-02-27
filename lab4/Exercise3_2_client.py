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
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Socket creation Failed. Error code: ' + str(msg[0]) + ', Message: ' + msg[1])
    sys.exit()
print('Socket created.')
host, port = socket.gethostname(), 1234
# Connect to the server
s.connect((host, port))
print('Successfully connected.')
random_generator = Random.new().read
client_key = RSA.generate(1024,random_generator)

server_publicKey = RSA.importKey(s.recv(2048))

key = 'Thisisakey123456'
symmetricKey = server_publicKey.encrypt(key.encode(), 32)
s.send(symmetricKey[0])

aes = AES.new(key, AES.MODE_ECB)
message = input("please type in the message to be send: ")
SpaceCount = len(message) + 16 - (len(message) % 16)
cipherText = aes.encrypt(message.ljust(SpaceCount))
s.send(cipherText)
s.close()
