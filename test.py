import hashlib
from legod import legod

def generate_md5(str):
    hl = hashlib.md5()
    # Tips
    # 此处必须声明encode
    # 否则报错为：hl.update(str)    Unicode-objects must be encoded before hashing
    hl.update(str.encode(encoding="utf-8"))
    return hl.hexdigest()

# print(generate_md5("161161Rpc"))
t = legod(True,"D:\\1Code\\legod-auto-pause\\")
t.login("17717615513","161161Rpc")
t.detection()
