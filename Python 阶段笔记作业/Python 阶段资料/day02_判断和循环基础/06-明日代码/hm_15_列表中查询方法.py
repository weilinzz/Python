my_list = ['小明', 18, 170.8, 3.14, True]

# index() 查找下标
# 查找 18 所在的下标
num = my_list.index(18)
print(num)  # 1
# 查找 20 所在的下标
# num1 = my_list.index(20)  # 代码会报错,原因是 数据不存在

# num2 = 20
# num2 = 18
num2 = 3.14
if num2 in my_list:
    num1 = my_list.index(num2)
    print(f'数据{num2}下标为', num1)
else:
    print(f"数据{num2}不存在")

# 统计出现的次数  count()
num3 = my_list.count(18)
print(num3)  # 1
num4 = my_list.count(19)
print(num4)  # 0


