# int
a = 10
# 不使用 = 不能改变数据值

# list
my_list = [1, 2, 3]

my_list.append(4)
print(my_list)

# dict
my_dict = {'name': 'xxx', 'age': 18}

del my_dict['age']
print(my_dict)
print('1', id(my_list), id(my_list[1]))
my_list[1] = 100
# 问: my_list 变量的引用是否发生改变
# 答: 没有改变 my_list 变量的引用, 因为只有= 可以改变变量的引用, 等号的左边 是 my_list[1]
# 所以, 等号修改的是 my_list中下标为 1 的位置的引用

print('2', id(my_list), id(my_list[1]))

