import socket
import struct

conn = socket.create_connection(('127.0.0.1', 2997))
l = [struct.unpack("<I", conn.recv(4))[0] for _ in xrange(4)]
conn.send(struct.pack("<I", sum(l) % 2**32))
print conn.recv(100)
