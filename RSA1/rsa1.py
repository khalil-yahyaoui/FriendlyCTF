# in this challenge, we have to encrypt a message using RSA 
# so the steps to do it are : 
# 1 - Convert the message to long (integer)
# 2 - compute N since we have p and q and N = p*q
# compute C which is m ** e mod n using python 
from Crypto.Util.number import bytes_to_long
m = b"Easy RSA"
m = bytes_to_long(m)

#I copied all params and put them into variables
e = 17
p = 15774638433564143093 
q = 12561850509256639879

# computing N
N = p * q

# computing C using pow method in python : pow(base,exponent,modulus)
C = pow(m,e,N)

print("Flag is Securinets{"+ str(c) + "}") #i used str method because we cannot concatenate string and numbers so i converted C to str first
