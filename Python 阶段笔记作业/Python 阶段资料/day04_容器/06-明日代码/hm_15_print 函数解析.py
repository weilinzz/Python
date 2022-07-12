# # print('hello world')
# # print('hello world', end='')
# # print('hello world', end=' ')
# print('hello world', end=' _*_ ')
# print('hello python')
#
# # 问题2
# print(1, 2, 3, 4, 5)  # 1 2 3 4 5
# print(1, 2, 3, 4, 5, sep=',')  # 1,2,3,4,5
# print(1, 2, 3, 4, 5, sep='\n')  #
# print(1, 2, 3, 4, 5, sep=' *_* ')  # 1 *_* 2 *_* 3 *_* 4 *_* 5
#
# print(1)
# print(1, 2)
# print(1, 2, 3)
# print(1, 2, 3, 4)


# 元组中的数据不能修改,因为修改的是列表中下标为 1 的位置内容
my_tuple = (1, 2, [3, 4])  # 元组存储的是 1 的地址 2 的地址和 列表的地址
my_tuple[-1][1] = 10
print(my_tuple)


