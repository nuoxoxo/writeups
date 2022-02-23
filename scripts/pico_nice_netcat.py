import socket

host = 'mercury.picoctf.net'
port = 49039
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(256).decode('utf-8').split()
L = [int(n) for n in data]
for c in L:
    print(chr(c), end='')
s.close()
