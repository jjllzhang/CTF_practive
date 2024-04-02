from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import gmpy2
import hashlib
from flag import FLAG

flag_plain = bytes_to_long(FLAG)


def main():
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    e = 65537
    phi = (p-1)*(q-1)
    d = gmpy2.invert(e,phi)
    flag_enc = encrypt(flag_plain,e,n)

    print "n = %d"%n
    print "e = %d"%e
    print "encrypted flag = %d"%flag_enc
    print "your ciphertext: "
    user_enc = int(raw_input())
    if user_enc==flag_enc:
        print "NO CHEAT"
        return
    user_plain = decrypt(user_enc,d,n)
    print "your plaintest: "
    print user_plain
    

def encrypt(p,e,n):
    return pow(p,e,n)

def decrypt(c,d,n):
    return pow(c,d,n)


if __name__=="__main__":
    main()


