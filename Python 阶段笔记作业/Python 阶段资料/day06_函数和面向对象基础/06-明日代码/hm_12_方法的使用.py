"""
类名: Game
属性: 玩家名字(name 实例属性)  top_score 类属性
方法
"""
import random


class Game:
    # 定义类属性, top_score ,记录游戏的最高分
    top_score = 0

    def __init__(self, name):
        self.name = name  # 玩家的名字

    # 定义静态方法
    @staticmethod
    def show_help():
        print('这是游戏的帮助信息')

    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    def start(self):
        # self.num = random.randint(10, 100)   # 作为属性
        num = random.randint(10, 100)  # 局部变量
        print(f"玩家 {self.name} 本次游戏得分为: {num}")
        if num > Game.top_score:
            # 修改历史最高分
            Game.top_score = num


# 创建对象
xw = Game('小王')
xw.show_top_score()
xw.start()
xw.show_top_score()
dh = Game('大黄')
dh.start()
dh.show_top_score()
