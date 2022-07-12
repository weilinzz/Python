"""
类名: Cat
属性: name(这个代码 探究在类外部添加属性,类内部添加暂时不管)
方法: eat( 输出: 小猫 xx 爱吃鱼,  xx 表示小猫具体的名字)
"""


# 1. 定义类
class Cat:
    # 定义方法
    def eat(self):
        print(f'小猫 {self.name} 爱吃鱼')


# 2. 创建对象
tom = Cat()
# 添加 name 属性
tom.name = "汤姆"
# 3. 调用方法
tom.eat()

# 创建对象 蓝猫
blue_cat = Cat()
blue_cat.name = '蓝猫'
blue_cat.eat()

# 问题
print(blue_cat.name)   # '蓝猫'
print(tom.name)   # "汤姆"
