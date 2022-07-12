my_list = ['郭德纲', '于谦', '岳云鹏', '郭麒麟', '张云雷', '孟鹤堂']
print(my_list)

# 1. 删除最后一个位置的数据
name = my_list.pop()
print(name)
print(my_list)

# 2. 删除下标为 3 的数据
name = my_list.pop(3)
print(name)
print(my_list)

# 删除下标为 10 的数据,没有这个下标
# my_list.pop(10)  # 代码报错, IndexError: pop index out of range

#  3. 删除 于谦 数据
my_list.remove('于谦')
print(my_list)


# 4. 将所有数据都删除
my_list.clear()
print(my_list)

