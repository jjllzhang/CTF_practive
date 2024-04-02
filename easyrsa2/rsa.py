from Crypto.Util.number import getPrime, bytes_to_long
from flag import FLAG

plain = bytes_to_long(FLAG)

p = getPrime(1024)
q1 = getPrime(1024)
q2 = getPrime(1024)
n1 = p*q1
n2 = p*q2

e = 65537
c1 = pow(plain,e,n1)
c2 = pow(plain,e,n2)

with open("enc.txt","wb") as f:
    f.write("n1 = "+str(n1)+"\n")
    f.write("c1 = "+str(c1)+"\n")
    f.write("n2 = "+str(n2)+"\n")
    f.write("c2 = "+str(c2)+"\n")
