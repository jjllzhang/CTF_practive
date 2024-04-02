from Crypto.Util.number import getPrime, bytes_to_long
import gmpy2
from flag import FLAG

plain = bytes_to_long(FLAG)

p = getPrime(1024)
q = gmpy2.next_prime(p+0xdddd)
n = p*q

e = 65537
c = pow(plain,e,n)

with open("enc.txt","wb") as f:
    f.write("n = "+str(n)+"\n")
    f.write("c = "+str(c)+"\n")
