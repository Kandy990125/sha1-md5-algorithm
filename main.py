# -*- coding= UTF-8 -*-
import hashlib

# 读出filename文件内的内容，此次实验中文件中储存的是要计算MD5值的16进制文本
# 返回值为filename文件下的文件内容

def fileopen(filename):
    f = open(filename)
    text = f.read()     # 读取文件内容
    text = bytes().fromhex(text)    # 将正常读取的字符串转化为16进制字符串
    # print(text)
    return text


# MD5类，文件初始化值包括需要计算MD5值的文本内容
# 包括一个md5_main函数，返回值为计算出的文本的md5值
class MD5:
    def __init__(self,text):
        self.text = text

    def md5_main(self):
        obj = hashlib.md5()     # 实例化
        obj.update(self.text)      # 对文本进行MD5值的计算
        return obj.hexdigest()      # 返回文本的MD5值

class SHA_1:
    def __init__(self,text):
        self.text = text

    def sha1_main(self):
        obj = hashlib.sha1()
        obj.update(self.text)
        return obj.hexdigest()
class SHA_256:
    def __init__(self,text):
        self.text = text

    def sha256_main(self):
        obj = hashlib.sha256()
        obj.update(self.text)
        return obj.hexdigest()
class SHA_512:
    def __init__(self,text):
        self.text = text

    def sha512_main(self):
        obj = hashlib.sha512()
        obj.update(self.text)
        return obj.hexdigest()
if __name__ == "__main__":
    text1 = fileopen("text1.txt")       # 读出text1.txt文本下的内容
    text2 = fileopen("text2.txt")       # 读出text2.txt文本下的内容
    print("--------------MD5--------------")
    md5 = MD5(text1)
    print(md5.md5_main())
    md5 = MD5(text2)
    print(md5.md5_main())
    print("-------------SHA-1-------------")
    sha1 = SHA_1(text1)
    print(sha1.sha1_main())
    sha1 = SHA_1(text2)
    print(sha1.sha1_main())
    print("------------SHA-256------------")
    sha256 = SHA_256(text1)
    print(sha256.sha256_main())
    sha256 = SHA_256(text2)
    print(sha256.sha256_main())
    print("------------SHA-512------------")
    sha512 = SHA_512(text1)
    print(sha512.sha512_main())
    sha512 = SHA_512(text2)
    print(sha512.sha512_main())