# 1. 定义一个动物类 Animal类, 方法: 吃
class Animal:
    def eat(self):
        print('饿了要吃东西....')


# 2. 定义一个狗类 Dog类,继承动物类
class Dog(Animal):
    # 2.2 在 Dog 类,定义叫的方法
    def bark(self):
        print('汪汪汪叫.....')


# 3. 定义一个哮天犬类, 继承狗类
class XTQ(Dog):
    pass


xtq = XTQ()
xtq.bark()  # 子类调用父类中方法
xtq.eat()  # 子类调用爷爷类的方法
