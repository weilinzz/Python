# 累加和: 1 + 2 + 3 + .... + 99 + 100
#
# 1. 定义一个变量保存求和的结果 num = 0
num = 0
# 2. 使用循环获取 1- 100 之间的数字
# 2.1 定义循环初始条件
i = 1
# 2.2 书写判断条件
while i <= 100:  # 如果 i 的值是 100, 也需要相加
    # 2.3. 在循环中进行求和
    num += i
    # 2.4 修改初始条件
    i += 1

# 打印求和结果, 打印一次,还是每次循环都打印 -->只打印最后一次,所以,要顶格书写,不能写在 while 的缩进中
print(f'求和的结果是: {num}')   # 5050
