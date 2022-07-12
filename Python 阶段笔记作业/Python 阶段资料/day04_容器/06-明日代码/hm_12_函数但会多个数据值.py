# 定义一个函数calc,可以返回两个数字的和以及两个数的差值
def calc(a, b):
    c = a + b
    d = a - b
    return c, d  # 会自动的组成元组进行返回


# 函数返回多个数据值,调用方式一,使用一个变量接收(元组)
result = calc(10, 20)
print(result, result[0], result[1])

# 拆包解包
m, n = calc(100, 200)
print(m, n)

