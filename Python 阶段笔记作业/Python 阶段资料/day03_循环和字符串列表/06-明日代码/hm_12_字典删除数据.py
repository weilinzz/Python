my_dict = {'name': '小明', 'age': 28, 'like': ['抽烟', '喝酒', '烫头', '学习'], 'sex': '男'}
print(my_dict)

# 1. 删除 sex 信息
del my_dict['sex']
print(my_dict)

# del my_dict['sex']  # 删除不存在的键值对 , KeyError: 'sex'

# 补充, 根据 指定的键值对
my_dict.pop('age')
print(my_dict)

# 删除一个爱好  抽烟
my_dict['like'].remove('抽烟')
print(my_dict)

# 清空
my_dict.clear()
print(my_dict)
