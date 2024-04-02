from Crypto.Util.number import getPrime, bytes_to_long
import gmpy2
from flag import FLAG

plain = bytes_to_long("\xdd"*128+FLAG)

def encrypt(plain):
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    assert(plain<n)
    e = 3
    c = pow(plain,e,n)
    assert(c!=plain**e)
    return (c,n)

with open("enc.txt","wb") as f:
    for _ in range(3):
        (c,n) = encrypt(plain)
        f.write("n = "+str(n)+"\n")
        f.write("c = "+str(c)+"\n")
