import socket
import sys
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
s.close()
