#AES is a symmetric-key block cipher , having the key and knowing the coorect mode you should be able to decrypt the ciphertext 
#The ECB mode encrypts each block seperately so if we have two identical plaintext blocks : it will give two identical ciphertext blocks
#we know from task description : the key , the ciphertext and the mode used to encrypt

from Crypto.Cipher import AES

ciphertext = bytes.fromhex("5b5d13f1157ebee75756296793d8b998497c7849aac925473dd875871f845b0e")
key = bytes.fromhex("4eb9b29b665a412894eef0692dda6735")

#Creating an AES instance and specifying the key and the mode
cipher = AES.new(key,AES.MODE_ECB)
print(cipher.decrypt(ciphertext))
