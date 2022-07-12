# 1, 打开文件
f = open('a.txt', 'r', encoding='utf-8')

# 2, 写文件
f.write('好好学习\n')
f.write('天天向上')
d = f.read()
print(d)
# 3, 关闭文件


