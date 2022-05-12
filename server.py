import socket
import os
from _thread import *

ServerSocket = socket.socket()
#host = '127.0.0.1'
host = socket.gethostbyname(socket.gethostname())
port = 1233
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
print(host)

ServerSocket.listen(5)


def threaded_client(connection,add):
    connection.send(str.encode('Welcome to the Servern'))
    while True:
        data = connection.recv(2048)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        else:
            # type(data)
            data = data.decode('utf-8')
            print(f'{add} : {data}')
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client,address ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()