my_list = ['郭德纲', '于谦', '岳云鹏', '郭麒麟', '张云雷', '孟鹤堂']

# 1. 将下标为 2 位置数据修改为 小岳岳
my_list[2] = '小岳岳'
print(my_list)

# 2. 将 '郭麒麟' 修改为大小姐
num = my_list.index('郭麒麟')
my_list[num] = '大小姐'
print(my_list)

# 修改 下标为 10 的位置的数据  --->下标不存在, 会报错
# my_list[10] = 'aaa'   # IndexError: list assignment index out of range
