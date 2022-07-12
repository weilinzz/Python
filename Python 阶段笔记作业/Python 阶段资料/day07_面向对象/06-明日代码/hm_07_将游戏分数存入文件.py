"""
Game 类,记录游戏的最高分,  问题: 每一次运行可以记录最高分,但上一次运行的分数没有了
想要将游戏的最高分保存到文件中 写文件操作
游戏开始的时候,应该从文件中读取历史最高分
"""
import random


class Game:
    # 定义类属性
    top_score = 0

    with open('score.txt', 'r', encoding='utf-8') as f:
        top_score = int(f.read())

    def __init__(self, name):
        self.name = name

    @staticmethod
    def show_help():
        print('这是游戏的帮助信息')

    @classmethod
    def show_top_score(cls):  # cls 就是类对象,就是类名
        # 打印输出游戏最高分 --> 访问类属性
        print(f"游戏最高分为 {cls.top_score}")

    def start_game(self):
        score = random.randint(10, 100)
        print(f'玩家 {self.name} 本次游戏得分为 {score}')
        # 判断本次得分和最高分之间的关系
        if score > Game.top_score:
            Game.top_score = score
            # 最高分改变的时候,需要将现在的最高分写入文件
            with open('score.txt', 'w', encoding='utf-8') as f:
                f.write(str(Game.top_score))


xw = Game('小王')
xw.start_game()
xw.show_top_score()
xw.start_game()
xw.show_top_score()


