from Crypto.Util.number import inverse,long_to_bytes

n = 227555533726794346965771272677917575629
c = 77962178294800447517109647217867140264
e = 65537
p = 12403119145035876589
q = 18346637734095243361

phi = (p-1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))