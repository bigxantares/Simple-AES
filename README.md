# Simple-AES-by-Python+QT
Simple AES encryption and decryption with a concise front-end interface is implemented in Python+QT, providing a simplified yet professional solution.
# 1.简介
根据"信息安全导论"课程第8-9次课讲述的AES算法，在课外认真阅读教科书附录D的内容，学习了解S-AES算法，使用Python+QT来编程实现加、解密程序。

开发平台:pycharm
# 2.算法标准设定
参考教科书《密码编码学于网络安全—原理与实践(第8版)》，附录D：简化AES。
# 3 主要功能
## 3.1 第1关：基本测试
程序提供GUI界面支持用户交互,支持输入16位数据和16位密钥，并输出16位密文

运行程序后有三种模式可以选择

![(F4AW}WH57P3V V@WY`8H5R](https://github.com/bigxantares/Simple-AES/assets/116985680/e5ae665f-2498-47b8-8e85-e75a306b1413)
### 加密功能示例（选择经典加密模式）
### 正常输入16bit数据和16bit密文，点击加密按钮：
![}EQZBH$64MH`GP$}B%(`7)D](https://github.com/bigxantares/Simple-AES/assets/116985680/121b24b2-a60f-446d-b0e5-323bba4f7384)

### 解密功能示例（选择经典加密模式）
### 使用加密的密钥和得到的密文能解密出原数据：
![DOMON~L38}2E4{C75UB5@RR](https://github.com/bigxantares/Simple-AES/assets/116985680/aa495cdc-1d5f-4285-8889-d490ebe3d1b6)

### 预防错误输入的提示示例：
在使用binary模式时，如果输入的二进制数量和格式不正确，会有错误提示：

![DXVBKR`432VVH7ZVEPU4Q13](https://github.com/bigxantares/Simple-AES/assets/116985680/cef36d74-c2dc-445c-8368-6a7495e5b6ab)  ![BT61R)D5$G}ADMSO7 56B{X](https://github.com/bigxantares/Simple-AES/assets/116985680/b0275c8f-9a0c-4c37-9aab-03530de1c974)

## 3.2 第2关：交叉测试
该项目能确保算法和程序在异构的系统或平台上都可以正常运行

设有A和B两组位同学，选择相同的密钥K，A、B组同学编写的程序对明文P进行加密后得到相同的密文C，B组同学接收到A组程序加密的密文C后，使用B组程序进行解密能得到与A相同的明文P

已知别的小组的明文、密钥和按正确加密流程得到的密文示例如下：

明文：0110111101101011 密钥：1010011100111011 密文：1111000110000110 
### 加密/解密验证：                                                                                                           
![IS1ZF WDE%QACPU5 ~L5QVT](https://github.com/bigxantares/Simple-AES/assets/116985680/a92cba4c-ef7c-4a35-9816-356bb4fdf490)  ![0)8I1W_Y{(O_I MGSRW6(K7](https://github.com/bigxantares/Simple-AES/assets/116985680/b3afd7e6-934a-4965-9689-b4a2474ccbe5)

## 3.3 第3关：扩展功能
考虑到向实用性扩展，加密算法的数据输入可以是ASII编码字符串(分组为2 Bytes)，对应地输出也可以是ACII字符串(很可能是乱码)。

### 加密/解密验证（切换为ASCII模式）：
![0((S{ MQ@KBTY C)KEQ2WA4](https://github.com/bigxantares/Simple-AES/assets/116985680/5716e724-0adf-482a-90c5-5dddb107817a)  ![6U II2IL2JAXYPB$DKYT80U](https://github.com/bigxantares/Simple-AES/assets/116985680/2667dbe0-9840-45d4-8cfd-5b47261fbe48)

## 3.4 第4关：多重加密

在主页面选择多重加密模式

![6TNEC{5698F}G}3X6J 3CPU](https://github.com/bigxantares/Simple-AES/assets/116985680/52da0b82-16b4-4935-82e5-aea28c53be9a)
### 3.4.1 双重加密将S-AES算法通过双重加密进行扩展，分组长度仍然是16 bits，但密钥长度为32 bits。
选择双重加密模式，进行加密解密的测试：

![)NOI2CQ1R1LH5Y XT8HDU5K](https://github.com/bigxantares/Simple-AES/assets/116985680/55f397ab-7681-4fdc-aa49-0ce097bc5a73)  ![$UIG@Y@EUDU} 66ZPT) YZU](https://github.com/bigxantares/Simple-AES/assets/116985680/b8beda2d-d80a-48c9-9a21-170a6c17e515)

### 3.4.2 中间相遇攻击假设你找到了使用相同密钥的明、密文对(一个或多个)，请尝试使用中间相遇攻击的方法找到正确的密钥Key(K1+K2)。
在循环中不断地生成随机的密钥，然后使用这些密钥key1对明文进行加密，然后用key2对密文进行解密，通过使用了Encrypy1(mingwen,key1)==Decrypy1(miwen,key2)来判断这两个结果是否相等，如果相等便打印出密钥（key1+key2）和用时，否则便打印未找到密钥和用时。

核心代码：

![image](https://github.com/bigxantares/Simple-AES/assets/116985680/f14567ea-666c-4084-aa99-4c7e3f56a435)

循环100次结果：

![image](https://github.com/bigxantares/Simple-AES/assets/116985680/a3780c22-47f3-4bb8-8f96-5c882504d217)

循环10000次结果：

![image](https://github.com/bigxantares/Simple-AES/assets/116985680/f00bdcfb-e160-48b8-b97a-290be1962659)

### 3.4.3 三重加密将S-AES算法通过三重加密进行扩展，下面两种模式选择一种完成：(1)按照32 bits密钥Key(K1+K2)的模式进行三重加密解密，(2)使用48bits(K1+K2+K3)的模式进行三重加解密。
这里使用第一种模式进行扩展

选择三重加密模式，进行加密解密测试：

![3(7ZWZUP5YP1AP%W8M)0P9Y](https://github.com/bigxantares/Simple-AES/assets/116985680/d34f2816-2a35-4a66-9b08-d27647fab4d8)  ![O7@@7CLOQ}E}$8%B{BVNK`W](https://github.com/bigxantares/Simple-AES/assets/116985680/60d9afbd-68b8-4198-91c5-f576d04d2f2e)

## 3.5 第5关：工作模式
基于S-AES算法，在较长的明文消息上使用密码分组链（CBC）模式进行加密

检验时，随机选定一组示例：明文为01101111011010111010011100111011 密钥为0110111101101011，本轮随机数为1111111111111111

### 进入CBC模式，进行加密：
![56X )UURUG`H`7FJ 950N13](https://github.com/bigxantares/Simple-AES/assets/116985680/ad08af2c-3fba-4fc7-b026-607c461be4d0)

得到结果密文：00110011010000111010011100110011
### 将结果和生成的随机数输入进行解密
![}(12(ZW@EDR(T$4TH @TVDT](https://github.com/bigxantares/Simple-AES/assets/116985680/a23424a1-f93a-447a-b668-0377a8b41443)

得到和已知明文相同的解密结果 01101111011010111010011100111011 

加密解密结果互相验证，证明使用密码分组链（CBC）模式完成三重加密解密成功。

### 在CBC模式下进行加密，并尝试篡改密文分组后进行解密，比较篡改前后的解密结果
沿用上述加解密的明文、密钥、随机数和密文，将密文篡改为：11111100001100111100110000010010 
### 解密结果如下所示：

此时解密所得的明文为01110110100001110000001101001010

我们逐位比较两个字符串的对应位置，判断差异：

01101111011010111010011100111011

01110110100001110000001101001010

区别分析： 在第4位、第5位、第7位等多个位置上出现差异。

# 使用说明
安装依赖：确保系统中已安装必要的依赖库和程序运行环境。
下载源代码：从项目仓库中下载源代码到本地。
编译程序：使用编译器对源代码进行编译，生成可执行文件。
运行程序：在环境中运行生成的可执行文件，打开GUI界面。

# 核心后端代码附录

## 基础函数实现

    # x^nfx函数
    def fx(xfx, a):
    if a[0] == 0:
        for i in range(3):
            xfx[i] = a[i + 1]
    else:
        xfx[1] = a[2]
        xfx[2] = 0 if a[3] == 1 else 1
        xfx[3] = 1

    # 使用的乘法群
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

    # 异或算法
    def yihuo8(a, b):
    t = [0] * 8
    for i in range(8):
        t[i] = a[i] ^ b[i]
    return t
    
    # 异或算法
    def yihuo4(a, b):
    t = [0] * 4
    for i in range(4):
        t[i] = a[i] ^ b[i]
    return t
    # 半字节代替
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
     # 逆反半字节代替
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
        
    # 行移位
    def zuoyi(temp):
    """
    temp是一个包含两个子列表的列表，每个子列表包含8个元素
    """
    # 注意半字节排列的方式，这里是第一字节的右半部分和第二字节的右半部分进行替换
    for i in range(4, 8):
        t = temp[1][i]
        temp[1][i] = temp[1][i - 4]
        temp[1][i - 4] = t
        
    # 行移位
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

    # 列混淆
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

    #  轮密钥加
    def lunmiyaojia(mingwen, key):
    for i in range(2):
        for j in range(8):
            mingwen[i][j] ^= key[i][j]

    # 加密实现
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
    
    # 逆反列混淆
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
        
    # 解密实现
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

## 具体源码请查看附录文件


