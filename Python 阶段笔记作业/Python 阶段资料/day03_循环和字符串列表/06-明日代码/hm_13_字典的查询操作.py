my_dict = {'name': '小明', 'age': 18}

# 获取 name 对应的值
print(my_dict['name'])

print(my_dict.get('name'))

# 获取 sex 的值
# print(my_dict['sex'])  # 代码报错,原因 键不存在 KeyError: 'sex'
print(my_dict.get('sex'))   # None
# 获取 sex 的值,如果不存在,返回 保密
print(my_dict.get('sex', '保密'))




