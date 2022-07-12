# 定义一个函数add, 对两个数字进行求和运算,并将求和的结果进行返回.
def add(a, b):
    c = a + b
    # 将求和的结果进行返回.
    return c


num = add(10, 20)
print('求和的结果:', num)
# 使用返回值得到这个结果之后,可以对这个数据值进行其他的操作
num += 100
print(num)
