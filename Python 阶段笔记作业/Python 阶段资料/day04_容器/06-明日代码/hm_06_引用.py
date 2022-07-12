a = 10
print(id(a))
b = a  # 将变量 a中存储的引用地址给了 b
print(id(b))

my_list = [1, 2, 3]
my_list1 = my_list  # 将变量 my_list 中存储的引用地址 给了 my_list1,
print(id(my_list))
print(id(my_list1))

my_list[1] = 100
print(my_list)
print(my_list1)

