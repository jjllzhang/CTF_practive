from Crypto.Util.number import getPrime, bytes_to_long
from gmpy2 import gcd, next_prime, invert
from flag import FLAG

plain = bytes_to_long(FLAG)

p = getPrime(1024)
q = getPrime(1024)
n = p*q
phi = (p-1)*(q-1)
d = getPrime(256)
while gcd(d,phi)!=1:
    d = next_prime(d)
e = invert(d,phi)
c = pow(plain,e,n)

with open("enc.txt","wb") as f:
    f.write("n = "+str(n)+"\n")
    f.write("e = "+str(e)+"\n")
    f.write("c = "+str(c)+"\n")

print p
print q
print d
