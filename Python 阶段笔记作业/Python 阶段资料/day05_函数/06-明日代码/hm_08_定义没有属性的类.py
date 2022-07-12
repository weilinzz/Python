# 1. 创建类
class Cat:
    # 定义方法, 在类的缩进中定义的函数就是方法
    def eat(self):  # self 暂时不管
        print('小猫爱吃鱼')

    def drink(self):
        print('小猫要喝水...')


# 2. 创建对象
# 变量 = 类名()
tom = Cat()

# 3. 对象调用类中的方法
# 对象.方法名()
tom.eat()
tom.drink()

blue_cat = Cat()
blue_cat.drink()
blue_cat.eat()
