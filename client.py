import socket
import time
import sys

s=socket.socket()
host=input(str("Please enter the hostname to connect"))
port=999
s.connect((host,port))
print("Connected to chat server")
while True:
    incoming_message=s.recv(1024)
    incoming_message=incoming_message.decode()
    print("JAYANT: ",incoming_message)
    message=input(str(">>"))
    message=message.encode()
    s.send(message)
    
