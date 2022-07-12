# 定义字典,包含键值对 姓名, 年龄, 爱好(抽烟 喝酒 烫头)
my_dict = {"name": '小明', 'age': 18, 'like': ['抽烟', '喝酒', '烫头']}
print(my_dict)

# 1. 添加 性别信息
my_dict['sex'] = '男'
print(my_dict)

# 2. 修改年龄为 28
my_dict['age'] = 28
print(my_dict)

# 3. 添加爱好 学习 ---> 向列表中添加数据
my_dict['like'].append('学习')
print(my_dict)

