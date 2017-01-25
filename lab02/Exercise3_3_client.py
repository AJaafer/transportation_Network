'''
xingeng wang
11144515
xiw031
'''

import socket
import sys

IPAddress = input("Please type the IP address: ")
port = input("Please type the port number: ")
ObjectPath = input("Please type the Object Path: ")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as msg:
    print('Socket creation Failed. Error code: ' + str(msg[0]) + ', Message: ' + msg[1])
    sys.exit()
print('Socket created.')
# Connect to the server
s.connect((IPAddress, int(port)))
print('Successfully connected.')
requestToSend = 'GET' + ' ' + '/' + ObjectPath + ' ' + 'HTTP/1.1'
s.send(requestToSend.encode())
print(s.recv(20480).decode())
s.close()