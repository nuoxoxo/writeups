import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'mercury.picoctf.net'
port = 49039
s.connect((host, port))
data = s.recv(256).decode('utf-8').split()
L = [int(n) for n in data]
for c in L: print(chr(c), end='')
s.close()
