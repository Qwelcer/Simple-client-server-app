# by Volkov Egor
import socket
import sys

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host='localhost'
port=80
msg=''

ip=socket.gethostbyname(host)

s.connect((ip, port))

print("Connected to Server")

while (msg!='exit'):
    msg=input("You: ")

    s.sendall(msg.encode('utf-8'))


s.close()
