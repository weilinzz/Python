# 1. 定义变量保存求和的结果
num = 0

# 2. 书写初始条件
j = 2  # 第一个偶数是 2

# 3. 书写循环
while j <= 100:
    # 4. 求和
    num += j
    # 改变初始条件, 确保每个数字都是偶数
    j += 2

print(f'求和的结果是: {num}')   #


