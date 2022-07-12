my_list = [[1, 2, 3], ['郭德纲', '于谦'], ['赵本山', '宋小宝']]

print(my_list[0])  # [1,2,3]
print(my_list[0][1])   # 2

print(my_list[1][1])  # '于谦'
print(my_list[1][1][1])  # '谦'

# 小

print(my_list[2][1][1])

my_list[0][1] = 100
print(my_list)  # [[1, 100, 3], ['郭德纲', '于谦'], ['赵本山', '宋小宝']]
my_list[2] = 10
print(my_list)   # [[1, 100, 3], ['郭德纲', '于谦'], 10]
# '郭德纲  ---> 小黑胖子
my_list[1][0] = '小黑胖子'
print(my_list)

my_list[1].append('aaa')
print(my_list)
