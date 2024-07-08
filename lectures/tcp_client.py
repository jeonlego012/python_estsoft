import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 10000))
s.send(b'hello')  # byte 단위로
data = s.recv(1024)
print(data)
s.close()
