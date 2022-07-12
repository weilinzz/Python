# 定义字符串
my_str = 'good good study day day up'
# 需求: 将字符串中的每个单词拆开
result = my_str.split()
print(result)  # ['good', 'good', 'study', 'day', 'day', 'up']

# 定义字符串
names = '小明,小王,小红,小张,小李'
# 需求,得到每一个名字
result1 = names.split(',')
print(result1)    # ['小明', '小王', '小红', '小张', '小李']

# 定义字符串,
my_str1 = "hello world and itcast and itheima and Python"

# 需求: 按照 and 字符串 进行切割
result2 = my_str1.split('and')
print(result2)   # ['hello world ', ' itcast ', ' itheima ', ' Python']
# 需求: 按照 and 字符串 进行切割1次
result3 = my_str1.split('and', 1)
print(result3)  # ['hello world ', ' itcast and itheima and Python']

