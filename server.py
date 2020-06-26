import socket
import sys
import time
s=socket.socket()
host=socket.gethostname()
print("Server will start on host: ",host)
port=999
s.bind((host,port))
print("Server has successfully binded to host and port")
print("Server is waiting for incoming connections")
s.listen(1)
conn,addr=s.accept()
print(addr," is connected to server and is online")
while True:    
    message=input(str(">>"))
    message=message.encode()
    conn.send(message)
    incoming_message=conn.recv(1024)
    incoming_message=incoming_message.decode()
    print("JAYANT: ",incoming_message)
