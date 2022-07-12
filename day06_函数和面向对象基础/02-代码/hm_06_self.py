"""
需求:小猫爱吃鱼，小猫要喝水, 定义不带属性的类
"""


class Cat:
    # 在缩进中书写 方法
    def eat(self):  # self 会自动出现,暂不管
        print(f'{id(self)}, self')
        print('小猫爱吃鱼...')


# 2. 创建对象
blue_cat = Cat()
blue_cat.eat()
