# the goal is to turn the is_admin=0 to is_admin=1
# This is a knwon attack called CBC bit flipping attack
# Since in CBC mode while decrypting, the decryption of the i-th block is xored with the (i-1)th block of ciphertext 
# so the length of our paylaod is 64 : luckily 64 % 16 = 0 
# and the byte we want to change is at the end of the last block of plaintext 
# so all we have to do is change the before last block in a way that gives us is_admin=1

# For more explanation about CBC bit flipping attack see this link :
# https://crypto.stackexchange.com/questions/66085/bit-flipping-attack-on-cbc-mode

from pwn import xor
payload = "name=M0NT4;category=Web;work=Hacker_fi_wa9et_l_faragh;is_admin=0"
login_token = bytes.fromhex("2bf77060ef918a4d2aae267e2aa47027ee2fd6c508040ddec70cae15e80a628bfe832e511b71990fc7e6f9d7cad7883a3e7ff06e5d95ee0ede3dc096d8b1540f")
#block size is 16

c1 = login_token[32:48]
tochange = xor(xor(c1[-1],b"0"),b"1")
c1 = c1[:15] + tochange
print(c1) 
#now we replace it

new_token = login_token[:32] + c1  + login_token[48:]
print(f"My new token is {new_token.hex()}")

# now all you have to do is send this token to the server and it will give u the flag
# flag is Securinets{Wlhy_keeeeeeesa7}
