## day02 作业题

## 简答

#### 1. 列举目前学过哪几种python的运算符?

```python

```

#### 2. 书写 if else 的语法格式?

```python

```

#### 3. 书写 if elif  else 的语法格式?

```python

```

## 代码题

### 题目1

#### 题干

用户输入年龄，如果年龄超过60岁，输出：可以退休了。

#### 答案

```python
# 书写答案

```



### 题目2

#### 题干

用户输入年龄，如果年龄超过60岁，输出："可以退休了"， 否则，输出："小伙子，加油干！"

#### 答案

```python
# 书写答案


```



### 题目3

#### 题干

用户输入年龄，按照如下标准书写程序，判断用户处于哪个年龄阶段，并提示：您的年龄是xx: 青少年/青年/中年/老年。

年龄段划分标准：0-17岁为青少年；18-35岁为青年；36-59为中年，60-99岁为老年。

#### 答案

```python
# 书写答案

```



### 题目4

#### 题干

用户登录输入验证码，已知验证码是`axyz`,  验证码正确输出 `可以登录`，否则输出：`验证码错误` 。

#### 答案

```python
# 书写答案


```



### 题目5

#### 题干

制作用户登录系统：已知A用户注册的用户名为`aaa`，密码是`123456`。具体要求如下：

登录时需要验证用户名、密码、验证码(固定验证码为`qwer`)。

提示：系统先验证验证码是否正确，正确后再验证用户名和密码。答案

```python
# 书写答案


```



### 题目 6

#### 设计一个程序:

- 1-7七个数字，分别代表周一到周日，
- 如果输入的数字是6或7，输出“周末”，否则输出“工作日”

#### 答案

```python 

```



### 题目 7

#### 设计一个程序:

- 1-7七个数字，分别代表周一到周日，
- 如果输入的数字是1，输出“今天是周一”
- 如果输入的数字是2，输出“今天是周二”
- 如果输入的数字是3，输出“今天是周三”
- 如果输入的数字是4，输出“今天是周四”
- 如果输入的数字是5，输出“今天是周五”
- 如果输入的数字是6或7，输出“今天是周末”

#### 答案 

```python 

```

### 题目 8

闰年判断程序(闰年是能被4整除，但不能被100整除的；或者能被400整除的年份)

输入一个有效的年份，判断是不是闰年

如果是闰年，则打印“xxxx年是闰年”；否则打印“xxxx年不是闰年”

如输入"2018"，将打印“2018年不是闰年”

#### 答案

```python 

```

### 题目 9

#### 题干

1. 书写代码求 `1-100之间所有数字的累加和`

2. 书写代码求 `1-100 之间奇数的累加和`

#### 答案

```python

```



### 题目10(提高)

#### 题干

设计简易计算器，可以进行基本的加减乘除运算, 参考如下

```python
请输出第一个数字: 
请输入第二个数字: 
请输入要进行的操作(+ - * /): 
计算的结果为:  
举例如下: 
请输出第一个数字: 10
请输入第二个数字: 20
请输入要进行的操作(+ - * /): + 
计算的结果为: 10 + 20 = 30 
```

#### 答案

```python

```

### 题目11 猜数字游戏(提高)

猜数字游戏：

1. 电脑产生一个（1-100）的随机数，用户进行猜测(通过 input 输入)，直到猜中为止。
2. 如果猜对了，输出：恭喜你猜对了，数字是 xx。
3. 如果猜的数字比随机数大，输出：猜测的数字太大了，继续加油
4. 如果猜测的数字比随机数小，输出：猜测的数字有点小，再来一次

```yacas 
应用知识点: 1. 循环  2. 随机数	3. break
```

#### 答案

```python

```

### 题目 12 过 7 游戏[稍难]

#### 题干

设计"过7 游戏” 程序,即在 1- 99 之间的数字中,如果数字 包含 7 或者是 7 的倍数,则输出"过...", 否则输出 具体的数字.

```python
如: 7 14 17 71 都输出过
```

```yacas
提示: 1. 使用循环获取 1-99 之间所有的数字, 2, 判断数字是否包含 7 或者是 7 的倍数
```

#### 答案

```python

```

