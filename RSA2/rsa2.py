#All we need to do is factor N using Factordb : http://factordb.com/
# This will give us p and q
from Crypto.Util.number import inverse

N = 833810193564967701912362955539789451139872863794534923259743419423089229206473091408403560311191545764221310666338878019
p = 863653476616376575308866344984576466644942572246900013156919
q = 965445304326998194798282228842484732438457170595999523426901 

e = 65537

# since we have the prime factorization of N : we can compute phi (Euler totient) 
#to read more about Euler totient : https://en.wikipedia.org/wiki/Euler%27s_totient_function
phi = (p-1)*(q-1)

#Since we computed phi we can now compute private key d as the inverse of e mod phi
d = inverse(e,phi)

print("Flag is Securinets{" + str(d) + "}")
