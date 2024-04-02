from Crypto.Util.number import getPrime, bytes_to_long
import gmpy2
from flag import FLAG

plain = bytes_to_long(FLAG)

p = getPrime(1024)
q = getPrime(1024)
n = p*q
e1 = 65537
e2 = 54049

c1 = pow(plain,e1,n)
c2 = pow(plain,e2,n)

with open("enc.txt","wb") as f:
    f.write("n = "+str(n)+"\n")
    f.write("c1 = "+str(c1)+"\n")
    f.write("c2 = "+str(c2)+"\n")
