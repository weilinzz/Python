my_str = "如果你给我的，和你给别人的是一样的，那我就不要了"

# 1. 需求:在 my_str 这个字符串中查找 你 的下标(查找第一个 使用最多)
num = my_str.find('你')
print(num)  # 2

# 2. 需求:在 my_str 这个字符串中查找 第二个 你 的下标

num1 = my_str.find('你', num+1)
print(num1)  # 8

# 3. 需求:在 my_str 这个字符串中查找 第三个 你 的下标
num2 = my_str.find('你', num1+1)
print(num2)  # -1, 没有找到,说明在这个字符串中,只有两个 你, 没有第三个
