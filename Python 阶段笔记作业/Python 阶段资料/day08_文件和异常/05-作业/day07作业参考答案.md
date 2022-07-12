## Day 07 作业题

## 简答题



### 1. 简述继承的语法?

```python
class 类B(类A):
    pass
# 类 B继承类 A
```

### 2. 为什么要重写,什么是重写,重写后如何调用父类的方法?

```python
# 为什么要重写
父类中的方法,不能满足子类对象的需求
# 什么是重写
子类实现了和父类同名的方法
# 重写后如何调用父类的方法
super().方法名()
```

## 代码题



### 课上代码完成-- 存放家具

![573DA0DC-0587-4FB7-85A8-CD85924B9EF8](day07作业.assets/573DA0DC-0587-4FB7-85A8-CD85924B9EF8.png)

```python

```





### 题目 1

定义一个学生类(Student): 

1. 包含属性 姓名`name`, 年龄`age`.

2. 包含方法: 

   1. 吃饭的方法`eat`, 在方法中输出`xx 要吃饭`, xx 为学生具体的名字
   2. 睡觉的方法`sleep`, 在方法输出`xx 要睡觉`, xx 为学生具体的名字
   3. 过年的方法`year`,  要求, 年龄增加一岁

3. 打印对象的时候, 输出 学生的 姓名和年龄信息格式如下

   `姓名: xxx, 年龄: xx 岁`, xx 为具体的名字和年龄

4. 创建两个对象, 并分别调用 吃饭和睡觉和过年的方法
   - 小明 18 岁
   - 小红  17 岁

```python
"""
类名: 学生类 Student
属性: 姓名 name, 年龄 age 
方法: 吃饭 eat 睡觉 sleep  过年 year  打印对象信息 __str__  添加属性 __init__
"""
class Stduent:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        
    def __str__(self):
        return f'姓名: {self.name}, 年龄: {self.age} 岁'
    
    def eat(self):
        print(f'{self.name} 要吃饭')
       	print('%s 要吃饭' % self.name)
        
    def sleep(self):
        print(f'{self.name} 要睡觉')
        
   	def year(self):
        self.age += 1
   

xm = Student('小明', 18)
print(xm)
xm.eat()
xm.sleep()
xm.year()
print(xm)
xh = Student('小红', 17)
xh.eat()
xh.sleep()
xh.year()
print(xh)
```



### 题目 2

定义一个电脑类(computer),

电脑有品牌(brand),有价格(price), 能播放电影(play_movie)。

分别创建2个对象"小米电脑 `mi`" 和 "苹果电脑 `mac`"。分别调用放电影的动作, 输出内容格式如下: `xx 播放电影 oo`, xx 为 电脑品牌, oo 为电影的名字, 电影名字作为参数传递即可

- 小米电脑播放 `葫芦娃`
- 苹果电脑 播放 `变形金刚`

```python
"""
类名: 电脑类 Computer
属性: 品牌 brand   价格 price 
方法: 放电影 play_movie
"""


class Computer:
    def __init__(self, brand, price):
        """初始化方法"""
        self.brand = brand  # 品牌
        self.price = price  # 价格

    def play_movie(self, movie_name):
        """播放电影的方法"""
        print("%s 电脑播放 %s " % (self.brand, movie_name))


# 使用类模板创建对象
mi = Computer("小米", 5000)
mi.play_movie("葫芦娃")

apple = Computer("苹果", 8000)
apple.play_movie("变形金刚")
```



### 题目 3

定义Animal动物类，具有 吃肉 `eat`的方法，喝 `drink`的方法，睡觉 `sleep`的方法
定义 狗Dog 继承了动物类，具有汪汪叫 `bark`的方法

- 狗去调用吃的方法
- 狗 去调用喝的方法

```python
class Animal:
    """动物类"""
    def eat(self):
        """吃方法"""
        print("动物都爱吃")

    def drink(self):
        """喝的方法"""
        print("动物可以喝水")

    def sleep(self):
        """睡觉的方法"""
        print("动物都喜欢睡觉")

class Dog(Animal):     # 单继承  子类名(父类名)
    """子类  狗类"""
    def bark(self):
        """狗叫的方法"""
        print("狗汪汪叫的方法")

# 创建子类对象
dog = Dog()
dog.bark()

dog.eat()   # 子类对象可以调用父类的方法
dog.drink()


```



