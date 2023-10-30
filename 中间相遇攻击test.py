
import random
import time

from encrypt import Decrypy1, Encrypy1
def attack():
    mingwen1='1010011100111011'
    miwen1='1000101010011100'
    mingwen = [[0 for _ in range(8)] for _ in range(2)]
    mingwen = [[int(mingwen1[i * 8 + j]) for j in range(8)] for i in range(2)]
    miwen = [[0 for _ in range(8)] for _ in range(2)]
    miwen = [[int(miwen1[i * 8 + j]) for j in range(8)] for i in range(2)]
    
    key1 = [[0 for _ in range(8)] for _ in range(2)]
    key2 = [[0 for _ in range(8)] for _ in range(2)]
    n=10000
    start_time=time.time()
    while n>0:
        n=n-1
        random_key1 = bin(random.randint(0, 2**16-1))[2:].zfill(16)
        random_key2 = bin(random.randint(0, 2**16-1))[2:].zfill(16)
        key1 = [[int(random_key1[i * 8 + j]) for j in range(8)] for i in range(2)]
        key2 = [[int(random_key2[i * 8 + j]) for j in range(8)] for i in range(2)]
        if Encrypy1(mingwen,key1)==Decrypy1(miwen,key2):
            end_time=time.time()
            print(f"找到密钥：{random_key1+random_key2},用时：{end_time-start_time}秒")
    end_time=time.time()
    print(f"未找到密钥,用时:{end_time-start_time}秒") 
attack()  