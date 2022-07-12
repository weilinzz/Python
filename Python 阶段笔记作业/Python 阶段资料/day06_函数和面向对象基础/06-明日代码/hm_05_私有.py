class Demo:
    def __init__(self, name, age):
        self.name = name
        # python 私有的本质是 修改属性的名字, 在私有属性名前添加 _类名 前缀
        self.__age = age  # 将 age 属性设置为私有的  # __age --> _Demo__age

    def __str__(self):
        return f"name: {self.name}, age: {self.__age}"  # __age --> _Demo__age


# 创建对象
a = Demo('大黄', 2)
print(a.name)  # name 是公有属性,可以在类外部使用
# print(a.__age)   # __age 是私有属性,不能在类外部使用
a.__age = 10  # 在类外部只能添加和修改公有属性, 添加一个公有属性,名字是 __age
print(a.__age)  # 访问的是公有属性 __age
print(a)  #
print(a._Demo__age)  # 2
a._Demo__age = 3
print(a)