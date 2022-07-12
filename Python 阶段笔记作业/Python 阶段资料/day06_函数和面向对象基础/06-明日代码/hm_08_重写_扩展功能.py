# 2. 定义一个狗类 Dog类,继承动物类
class Dog:
    # 2.2 在 Dog 类,定义叫的方法
    def bark(self):
        print('汪汪汪叫.....')


# 3. 定义一个哮天犬类, 继承狗类
class XTQ(Dog):
    def bark(self):
        super().bark()
        # 书写扩展的新功能
        print('看见主人摇尾巴...')


xtq = XTQ()
xtq.bark()

