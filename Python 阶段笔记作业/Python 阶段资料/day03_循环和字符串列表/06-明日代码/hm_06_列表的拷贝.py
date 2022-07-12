my_list = [1, 4, 3.14, 'aa']

my_list1 = my_list.copy()
# my_list1 = my_list   # 赋值, 不是拷贝,两个变量,但是是一个列表

print('my_list :', my_list)  # my_list : [1, 4, 3.14, 'aa']
print('my_list1:', my_list1)   # my_list : [1, 4, 3.14, 'aa']

my_list1[1] = 100

print('my_list :', my_list)  # my_list : [1, 4, 3.14, 'aa']
print('my_list1:', my_list1)   # my_list1: [1, 100, 3.14, 'aa']
