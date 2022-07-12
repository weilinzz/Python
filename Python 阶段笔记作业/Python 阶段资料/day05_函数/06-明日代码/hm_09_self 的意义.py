# 1. 创建类
class Cat:
    # 定义方法, 在类的缩进中定义的函数就是方法
    def eat(self):  # self 暂时不管
        print(f'self: {id(self)}')
        print('小猫爱吃鱼')


# 2. 创建对象
# 变量 = 类名()
tom = Cat()
print(f"tom : {id(tom)}")
# 3. 对象调用类中的方法
# 对象.方法名()
tom.eat()  # tom 调用方法, 将 tom 引用传递给 self

blue_cat = Cat()
print(f"blue: {id(blue_cat)}")

blue_cat.eat()  # blue_cat 调用方法,将 blue_cat 对象的引用传递给 self
