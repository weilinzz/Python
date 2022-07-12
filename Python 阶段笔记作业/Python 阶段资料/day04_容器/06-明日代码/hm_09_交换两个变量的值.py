a = 10
b = 20

# 方法一, 使用第三个变量
# c = a  # c 的值 10
# a = b  # a 的值 20
# b = c  # b 的值 10

# print(a, b)

# 方法二, 使用数学中的方法
# a = a + b  # a 的值 30
# b = a - b  # b 的值 10
# a = a - b  # a 的值 20
#
# print(a, b)

# 方法三, python 特有的方法,
# a, b = b, a
# print(a, b)

cc = b, a  # 将两个数据值组成元组给到一个变量, 组包
print(type(cc), cc)  # <class 'tuple'> (20, 10)

a, b = cc
print(a, b)


