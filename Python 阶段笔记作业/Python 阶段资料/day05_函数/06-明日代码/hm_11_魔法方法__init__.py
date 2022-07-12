# 1. 定义类
class Cat:
    def __init__(self):
        # 正常的代码是在这里添加属性的,但是目前我们打印输出一句话
        print('我是__init__ 方法,我被调用了')

    # 定义方法
    def eat(self):
        print(f'小猫 爱吃鱼')


# Cat()  # 是创建对象
# tom = Cat  # 不是创建对象, 将类的引用给 tom 了, 意思是 tom 也是类了
tom = Cat()  # 是创建对象

cat = tom  # 不是创建对象

