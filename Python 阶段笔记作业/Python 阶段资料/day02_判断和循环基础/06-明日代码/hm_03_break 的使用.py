# while 循环, 吃了三个之后吃饱了
# i = 0
#
# while i < 5:
#     print('吃了一个苹果')
#     i += 1  # 吃苹果的个数加1
#     if i == 3:
#         print('吃饱了,后续苹果不吃了')
#         # 即这个条件满足, 后续的循环不再执行
#         break


# for 循环实现
# for i in range(5):  # 0 1 2 3 4
#     print('吃了一个苹果')
#     if i == 2:  # 先吃后判断
#         print('吃饱了,不吃了')
#         break


for i in range(5):  # 0 1 2 3 4
    # 先判断后吃
    if i == 3:
        print('吃饱了,不吃了')
        break
    print('吃了一个苹果')

