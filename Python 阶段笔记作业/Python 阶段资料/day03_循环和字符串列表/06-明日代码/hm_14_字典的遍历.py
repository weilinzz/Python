my_dict = {'name': '小王', 'age': 18, 'sex': '男'}

# 遍历字典的键
for k in my_dict:
    print(k)

for k in my_dict.keys():
    print(k)

print('-' * 30)   # 字符串 * 整数,将字符串重复多少遍
print('_*_ ' * 30)   # 字符串 * 整数,将字符串重复多少遍

# 遍历字典的值
for v in my_dict.values():
    print(v)

print('*' * 30)
# 遍历键值对
for k, v in my_dict.items():
    print(k, v)

