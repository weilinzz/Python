# for i in range(5):  # 0 1 2 3 4
#     print(f'准备吃编号为{i} 的苹果-----')
#     if i == 2:
#         print('咦. 有半条虫子,这个苹果不吃了,继续吃下一个...')
#         continue
#     print(f'正在吃编号为{i} 的苹果')

i = 0
while i < 5:
    print(f'准备吃编号为{i} 的苹果-----')
    if i == 2:
        print('咦. 有半条虫子,这个苹果不吃了,继续吃下一个...')
        i += 1
        continue
    print(f'正在吃编号为{i} 的苹果')
    i += 1
