from Crypto.Util.number import inverse, long_to_bytes

def calculate_c_new(n, e, encrypted_flag, r):
    # 计算r的加密版本
    re = pow(r, e, n)
    # 创建新的密文
    c_new = (encrypted_flag * re) % n
    return c_new

def decrypt_flag(m_new, r, n):
    # 计算原始flag
    flag = (m_new * inverse(r, n)) % n
    return long_to_bytes(flag)

def main():
    # 第一阶段：生成c_new并发送给服务器
    n = int(input("请输入n: "))
    e = int(input("请输入e: "))
    encrypted_flag = int(input("请输入加密的flag: "))
    r = 2  # 实际情况下，r需要是一个与n互质的随机数

    c_new = calculate_c_new(n, e, encrypted_flag, r)
    print("请将此c_new发送给服务器: ", c_new)
    print("完成第一阶段，请将服务器返回的m_new输入。")

    # 第二阶段：用户输入m_new，计算并显示flag
    m_new = int(input("请输入m_new: "))
    flag = decrypt_flag(m_new, r, n)
    print("Flag是: ", flag.decode())

if __name__ == "__main__":
    main()
