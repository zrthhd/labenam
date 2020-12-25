import socket

ClientSocket = socket.socket()
host = '192.168.0.135'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))



Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))

while True:
    Input = input('')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))


ClientSocket.close()
