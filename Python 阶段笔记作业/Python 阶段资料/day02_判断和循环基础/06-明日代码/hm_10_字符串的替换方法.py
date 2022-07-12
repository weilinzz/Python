# 定义一个字符串
my_str = 'good good study'

# 需求: 1. 将 good 全部替换为 GOOD
my_str1 = my_str.replace('good', "GOOD")
print('my_str :', my_str)
print('my_str1:', my_str1)

# 需求 2: 将 my_str 中的 第一个 'good 替换为 "GOOD"
my_str2 = my_str.replace('good', 'GOOD', 1)
print('my_str2:', my_str2)

# 需求 3: 只将第二个 good 替换 GOOD
# 3.1 先替换两个 GOOD
my_str3 = my_str.replace('good', 'GOOD', 2)
# 3.2 再讲第一个 替换 为 good
my_str4 = my_str3.replace('GOOD', 'good', 1)
print('my_str4:', my_str4)

