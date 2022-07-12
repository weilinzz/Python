with open('a.txt', 'r', encoding='utf-8') as f:
    buf = f.readline()
    print(buf)
    buf = f.readline()
    print(buf)


print('-' * 30)

with open('a.txt', 'r', encoding='utf-8') as f:
    # 不知道文件有多少行,想要全部读取,使用循环
    while True:
        buf = f.readline()
        if len(buf) == 0:  # ""
            break
        print(buf, end='')