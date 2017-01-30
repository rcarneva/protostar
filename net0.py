import socket
import struct

conn = socket.create_connection(('127.0.0.1', 2999))
i = int(conn.recv(1000).split("'")[1])
conn.send(struct.pack("<I", i))

print conn.recv(1000)
