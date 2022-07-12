# 需求:
# 1. 使用 input 函数获取一个字符串
my_str = input('请输入一个字符串:')

# 2. 遍历这个字符串,输出本次遍历到的这个字符
for i in my_str:
    # 3. 如果这个字符是 'q',则终止循环
    if i == 'q':
        break
    # 4. 如果这个字符是 'e', 不输出这个字符,输出 '字符e跳过不输出'
    elif i == 'e':
        print('字符e跳过不输出')
        continue
    print(i)
