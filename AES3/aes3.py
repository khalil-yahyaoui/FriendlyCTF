#The first step into solving this task is to find out the IV
#when decrypting in CBC : the first block is decrypted and then xored with IV to get plaintext
# and since we have the plaintext and the ciphertext we can find the iv : let's note b1 : first block of plaintext and c1 is the first block of ciphertext and D is the AES function
# that decrypts : then we have b1 = D(c1) xor IV  => IV = b1 xor D(c1)
#Note : block size is 16

from Crypto.Cipher import AES
from pwn import xor

key = bytes.fromhex("914792533f171cc529aded1a79034519")
b1 = b"The flag is Securinets{"[:16]
c = bytes.fromhex("a3cfa5dc696cc041cf9cb5b2a3055290739bd8c1b7d1e6df76d02dd893dba5bba6148a147b402dafbdbfe74a5c221e1665eb9644afb6daee5d1f2313ffafdcd6")
c1 = c[:16]
cipher = AES.new(key,AES.MODE_ECB) # we could also do AES.new(key,AES.MODE_CBC,b"\x00"*16) because xoring with null bytes will be the same as not xoring at all 
IV = xor(b1 , cipher.decrypt(c1))

#now we have the key and IV we can decrypt out ciphertext
cipher = AES.new(key,AES.MODE_CBC,IV)
print(cipher.decrypt(c))
