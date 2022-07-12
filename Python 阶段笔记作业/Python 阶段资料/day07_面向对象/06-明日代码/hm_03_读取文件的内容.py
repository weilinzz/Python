# 1. 打开文件
# 1.1 a.txt 当前目录下的 a.txt, 目前没有, 读打开文件,文件不存在,会报错
f = open('a.txt', 'r', encoding='utf-8')
# 2. 读 文件
buf = f.read()
print(buf)
# 3. 关闭文件
f.close()


