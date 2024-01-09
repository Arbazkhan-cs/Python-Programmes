import socket

client_1 = socket.socket()

client_1.connect(('localhost', 9999))

name = input("Enter Your Name: ")
client_1.send(bytes(name, 'utf-8'))

print(client_1.recv(1024).decode())

client_1.send(bytes("Hello World", 'utf-8'))

