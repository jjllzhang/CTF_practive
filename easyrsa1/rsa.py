from Crypto.Util.number import getPrime, bytes_to_long
from flag import FLAG

plain = bytes_to_long(FLAG)

p = getPrime(64)
q = getPrime(64)
n = p*q
e = 65537
c = pow(plain,e,n)

with open("enc.txt","wb") as f:
    f.write("n = "+str(n)+"\n")
    f.write("e = "+str(e)+"\n")
    f.write("c = "+str(c)+"\n")
print("q = "+str(q))
print("p = "+str(p))
print("your flag is: "+FLAG+"\n")
