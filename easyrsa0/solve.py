from Crypto.Util.number import inverse

n = 99145550571841
e = 65537
c = 96034585716955
p = 9589753
q = 10338697

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, n)
print(m)