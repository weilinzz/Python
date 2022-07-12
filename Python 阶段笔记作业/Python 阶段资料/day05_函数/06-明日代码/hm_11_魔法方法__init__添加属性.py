# 1. 定义类
class Cat:
    def __init__(self, name):
        # self.属性名 = 属性值
        self.name = name

    # 定义方法
    def eat(self):
        print(f'小猫 {self.name} 爱吃鱼')


tom = Cat('汤姆')  # 是创建对象, 给 tom 对象 添加属性 汤姆
tom.eat()  # 将 tom 对象 传递给 self,即 self 就是 tom

blue_cat = Cat('蓝猫')
blue_cat.eat()

black_cat = Cat('黑猫')
black_cat.eat()  #


