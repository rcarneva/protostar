import socket
import struct
from itertools import izip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return izip_longest(*args, fillvalue=fillvalue)

conn = socket.create_connection(('127.0.0.1', 2999))
i = int(conn.recv(1000).split("'")[1])

s = hex(i)[2:]

i = int(''.join(map(''.join, list(grouper(s, 2))[::-1])), 16)

conn.send(struct.pack(">I", i))

print conn.recv(1000)
