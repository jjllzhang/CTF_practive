from Crypto.Util.number import getPrime
from flag import FLAG

#0ops{**********}
assert FLAG[:5]=="0ops{"
assert FLAG[-1]=="}"
plain = int(FLAG[5:-1])

p = getPrime(24)
q = getPrime(24)
n = p*q
e = 65537
c = pow(plain,e,n)

with open("enc.txt","wb") as f:
    f.write("n = "+str(n)+"\n")
    f.write("e = "+str(e)+"\n")
    f.write("c = "+str(c)+"\n")

print("your flag is: 0ops{"+str(plain)+"}")
