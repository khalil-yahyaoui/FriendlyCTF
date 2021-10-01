#Using the xor property found in the chall description and the pwntools module in python we can find our flag
#Since we don't know the key used to encrypt the flag , all we have to do is bruteforce it.

from pwn import xor

c = bytes.fromhex("31070117100b0c071611190010171607040d1001073d01030c3d00100703093d1a0d103d110d0f07160b0f07111f") # convert from hex to bytes

for i in range(256) : # we are going to bruteforce all the ascii
	flag = xor(c,chr(i).encode())
	if b"Securinets{" in flag : 
		print(f"Flag is {flag}")
		break
