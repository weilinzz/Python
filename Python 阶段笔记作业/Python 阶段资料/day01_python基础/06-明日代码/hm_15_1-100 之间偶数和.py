# 1. 定义一个变量保存求和的结果
num = 0

# 2 定义循环初始条件
j = 1

# 3. 书写循环
while j <= 100:
    # 4. 判断这个数字是不是偶数
    if j % 2 == 0:
        # 表示是偶数, 相加求和
        num += j

    # 5. 改变初始条件
    j += 1


print(f'求和的结果是: {num}')   #

