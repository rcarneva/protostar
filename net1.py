import socket
import struct

conn = socket.create_connection(('127.0.0.1', 2998))
s = conn.recv(100)
conn.send(str(struct.unpack("<I", s)[0]) + "\n")

print conn.recv(1000)
