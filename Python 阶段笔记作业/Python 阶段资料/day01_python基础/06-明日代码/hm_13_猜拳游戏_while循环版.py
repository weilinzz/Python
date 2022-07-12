# import random
#
# while True:
#     # 1. 从控制台输入要出的拳 —— 石头(1)/剪刀(2)/布(3)
#     player = int(input('请输入要出的拳:石头(1)/剪刀(2)/布(3):'))   # str
#     # 2. 电脑随机出拳
#     computer = random.randint(1, 3)
#     # 3. 比较胜负
#     if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
#         print('恭喜你,你赢了')
#     elif player == computer:
#         print('平局, 不要走,大战三百回合')
#     else:
#         print('弱爆了,连电脑都赢不了')


import random

#  1. 定义初始变量
i = 0

# 2. 书写循环
while i < 5:
    # 1. 从控制台输入要出的拳 —— 石头(1)/剪刀(2)/布(3)
    player = int(input('请输入要出的拳:石头(1)/剪刀(2)/布(3):'))   # str
    # 2. 电脑随机出拳
    computer = random.randint(1, 3)
    # 3. 比较胜负
    if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
        print('恭喜你,你赢了')
    elif player == computer:
        print('平局, 不要走,大战三百回合')
    else:
        print('弱爆了,连电脑都赢不了')

    # 4. 改变计数器
    i += 1


