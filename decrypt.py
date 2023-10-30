
# s盒
s = [
    [9, 4, 10, 11],
    [13, 1, 8, 5],
    [6, 2, 0, 3],
    [12, 14, 15, 7]
]

# 逆s盒
ns = [
    [10, 5, 9, 11],
    [1, 7, 8, 15],
    [6, 0, 2, 3],
    [12, 4, 13, 14]
]

# 替换盒
tihuanwei = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]

# 轮常数
rcon1 = [1, 0, 0, 0, 0, 0, 0, 0]
rcon2 = [0, 0, 1, 1, 0, 0, 0, 0]



# 实现x ^ nfx的函数
def fx(xfx, a):
    if a[0] == 0:
        for i in range(3):
            xfx[i] = a[i + 1]
    else:
        xfx[1] = a[2]
        xfx[2] = 0 if a[3] == 1 else 1
        xfx[3] = 1


def chengfa(a, b):
    """
    a和b是长度为4的整数列表
    """
    # 储存结果的系数
    result = [0] * 4

    # 记录下x^nfx
    xfx = [0] * 4
    fx(xfx, a)
    x2fx = [0] * 4
    fx(x2fx, xfx)
    x3fx = [0] * 4
    fx(x3fx, x2fx)

    # 现在需要根据多项式a和b开始异或
    if b[0] == 1:
        for i in range(4):
            result[i] ^= x3fx[i]
    if b[1] == 1:
        for i in range(4):
            result[i] ^= x2fx[i]
    if b[2] == 1:
        for i in range(4):
            result[i] ^= xfx[i]
    if b[3] == 1:
        for i in range(4):
            result[i] ^= a[i]

    return result

def yihuo8(a, b):
    t = [0] * 8
    for i in range(8):
        t[i] = a[i] ^ b[i]
    return t

def yihuo4(a, b):
    t = [0] * 4
    for i in range(4):
        t[i] = a[i] ^ b[i]
    return t

def s_he_tihuan(temp):
    """
    temp是包含8个元素的整数列表
    """
    t1 = 2 * temp[0] + temp[1]
    t2 = 2 * temp[2] + temp[3]
    t3 = 2 * temp[4] + temp[5]
    t4 = 2 * temp[6] + temp[7]
    tihuan1 = s[t1][t2]  # 记录替换后的数字
    tihuan2 = s[t3][t4]
    # 四位四位进行替换
    for i in range(4):
        temp[i] = tihuanwei[tihuan1][i]
    for i in range(4):
        temp[i + 4] = tihuanwei[tihuan2][i]

def ns_he_tihuan(temp):
    """
    temp是包含8个元素的整数列表
    """
    t1 = 2 * temp[0] + temp[1]
    t2 = 2 * temp[2] + temp[3]
    t3 = 2 * temp[4] + temp[5]
    t4 = 2 * temp[6] + temp[7]
    tihuan1 = ns[t1][t2]  # 记录替换后的数字
    tihuan2 = ns[t3][t4]
    # 四位四位进行替换
    for i in range(4):
        temp[i] = tihuanwei[tihuan1][i]
    for i in range(4):
        temp[i + 4] = tihuanwei[tihuan2][i]

def zuoyi(temp):
    """
    temp是一个包含两个子列表的列表，每个子列表包含8个元素
    """
    # 注意半字节排列的方式，这里是第一字节的右半部分和第二字节的右半部分进行替换
    for i in range(4, 8):
        t = temp[1][i]
        temp[1][i] = temp[1][i - 4]
        temp[1][i - 4] = t

def g(temp, rcon):
    """
    temp是一个包含8个元素的数组，rcon是轮常数
    返回一个包含8个元素的列表
    """
    # 注意这个temp是密钥，不能改动，要复制一个新的进行计算
    t = temp.copy()

    # 循环左移
    for i in range(4):
        tt = t[i + 4]
        t[i + 4] = t[i]
        t[i] = tt

    # 进行s盒替换
    s_he_tihuan(t)

    # 进行轮常数异或
    return yihuo8(t, rcon)


def liehunxiao(mingwen):
    si_de2jinzhi = [0, 1, 0, 0]
    m00 = [0] * 4
    m10 = [0] * 4
    m01 = [0] * 4
    m11 = [0] * 4

    for i in range(4):
        m00[i] = mingwen[0][i]
        m10[i] = mingwen[0][i + 4]
        m01[i] = mingwen[1][i]
        m11[i] = mingwen[1][i + 4]

    n00 = [0] * 4
    n10 = [0] * 4
    n01 = [0] * 4
    n11 = [0] * 4

    n00 = yihuo4(m00, chengfa(si_de2jinzhi, m10))  # 乘法结果是1011
    n10 = yihuo4(chengfa(si_de2jinzhi, m00), m10)  # 0101
    n01 = yihuo4(m01, chengfa(si_de2jinzhi, m11))  # 0100
    n11 = yihuo4(chengfa(si_de2jinzhi, m01), m11)  # 0010

    for i in range(4):
        mingwen[0][i] = n00[i]
        mingwen[0][i + 4] = n10[i]
        mingwen[1][i] = n01[i]
        mingwen[1][i + 4] = n11[i]


def lunmiyaojia(mingwen, key):
    for i in range(2):
        for j in range(8):
            mingwen[i][j] ^= key[i][j]


def Encrypy(mingwen, key):
    # 输入明文和密钥
    # 密钥扩展算法，由于只有三轮加密，第一轮还只使用了原始key
    key1 = [[0 for _ in range(8)] for _ in range(2)]
    key2 = [[0 for _ in range(8)] for _ in range(2)]
    key1[0] = yihuo8(key[0], g(key[1], rcon1))
    key1[1] = yihuo8(key1[0], key[1])
    key2[0] = yihuo8(key1[0], g(key1[1], rcon2))
    key2[1] = yihuo8(key2[0], key1[1])
    print("mingwen：", mingwen)
    print("k：", key)
    print("k1：", key1)
    print("k2：", key2)
    # 第0轮的轮密钥加
    lunmiyaojia(mingwen, key)
    print("处理后的结果为：", mingwen)
    # 第一轮
    # 明文半字节代替
    s_he_tihuan(mingwen[0])
    s_he_tihuan(mingwen[1])
    print("处理后的结果为：", mingwen)
    # 明文的行移位
    zuoyi(mingwen)
    print("处理后的结果为：", mingwen)
    # 明文的列混淆
    liehunxiao(mingwen)
    print("处理后的结果为：", mingwen)
    # 明文的轮密钥加
    lunmiyaojia(mingwen, key1)
    print("处理后的结果为：", mingwen)
    # 第二轮
    # 明文半字节代替
    s_he_tihuan(mingwen[0])
    s_he_tihuan(mingwen[1])
    print("处理后的结果为：", mingwen)
    # 明文的行移位
    zuoyi(mingwen)
    print("处理后的结果为：", mingwen)
    # 明文的轮密钥加
    lunmiyaojia(mingwen, key2)
    print("处理后的结果为：", mingwen)
    # 现在的明文其实是密文了
    # 将明文的二维列表转换为字符串
    encrypted_text = ""
    for row in mingwen:
        for item in row:
            encrypted_text += str(item)
    return encrypted_text

# 逆列混肴
def n_liehunxiao(miwen):
    nijuzhen2 = [0, 0, 1, 0]
    nijuzhen9 = [1, 0, 0, 1]
    m00 = [0] * 4
    m10 = [0] * 4
    m01 = [0] * 4
    m11 = [0] * 4

    for i in range(4):
        m00[i] = miwen[0][i]
        m10[i] = miwen[0][i + 4]
        m01[i] = miwen[1][i]
        m11[i] = miwen[1][i + 4]

    n00 = [0] * 4
    n10 = [0] * 4
    n01 = [0] * 4
    n11 = [0] * 4

    n00 = yihuo4(chengfa(nijuzhen9, m00), chengfa(nijuzhen2, m10))
    n10 = yihuo4(chengfa(nijuzhen2, m00), chengfa(nijuzhen9, m10))
    n01 = yihuo4(chengfa(nijuzhen9, m01), chengfa(nijuzhen2, m11))
    n11 = yihuo4(chengfa(nijuzhen2, m01), chengfa(nijuzhen9, m11))

    for i in range(4):
        miwen[0][i] = n00[i]
        miwen[0][i + 4] = n10[i]
        miwen[1][i] = n01[i]
        miwen[1][i + 4] = n11[i]

def Decrypy(miwen, key):
    key1 = [[0 for _ in range(8)] for _ in range(2)]
    key2 = [[0 for _ in range(8)] for _ in range(2)]
    key1[0] = yihuo8(key[0], g(key[1], rcon1))
    key1[1] = yihuo8(key1[0], key[1])
    key2[0] = yihuo8(key1[0], g(key1[1], rcon2))
    key2[1] = yihuo8(key2[0], key1[1])
    print("miwen：", miwen)
    print("k：", key)
    print("k1：", key1)
    print("k2：", key2)
    # 第2轮的明文轮密钥加的逆操作
    lunmiyaojia(miwen, key2)
    print("处理后的结果为：", miwen)
    # 第2轮的明文的行移位逆操作
    zuoyi(miwen)
    print("处理后的结果为：", miwen)
    # 第2轮的明文的半字节代替的逆操作
    ns_he_tihuan(miwen[1])
    ns_he_tihuan(miwen[0])
    print("处理后的结果为：", miwen)
    # 第1轮的明文轮密钥加的逆操作
    lunmiyaojia(miwen, key1)
    print("处理后的结果为：", miwen)
    # 第1轮的明文的列混淆的逆操作
    n_liehunxiao(miwen)
    print("处理后的结果为：", miwen)
    # 第1轮的明文的行移位的逆操作
    zuoyi(miwen)
    print("处理后的结果为：", miwen)
    # 第1轮明文半字节代替的逆操作
    ns_he_tihuan(miwen[1])
    ns_he_tihuan(miwen[0])
    print("处理后的结果为：", miwen)
    # 第0轮的轮密钥加的逆操作
    lunmiyaojia(miwen, key)
    print("处理后的结果为：", miwen)
    # 现在的密文其实是解密后的明文了
    # 将明文的二维列表转换为字符串
    plaintext = ""
    for row in miwen:
        for item in row:
            plaintext += str(item)
    return plaintext

