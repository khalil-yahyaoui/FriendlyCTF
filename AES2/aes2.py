#AES CBC mode is another mode that doesn't work the same as ECB : 
# CBC mode encrypts each block and xor it with the previous ciphertext block , since the first block doesn't have a previous block , we use the IV

from Crypto.Cipher import AES

ciphertext = bytes.fromhex("9724b7519b578188a0a8f9321fed349f5e553900f3121b74e4dc732010b0b9160611b0d639ff95a3f3f15d6a8097ec97")
iv = bytes.fromhex("366cea9b59733fec3d1503658cfb3c0e")
key = bytes.fromhex("9ffdf56be67a5d6aec701b27bfd6c589")

cipher = AES.new(key,AES.MODE_CBC,iv)
print(cipher.decrypt(ciphertext))
