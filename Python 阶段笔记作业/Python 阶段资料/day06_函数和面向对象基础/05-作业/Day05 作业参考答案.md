## Day05 作业

## 简答

### 1. 函数定义和调用的语法格式?

```Python
# 函数定义
def 函数名(参数, ...):
    pass

# 函数调用
函数名(参数)
```

### 2. 简述什么是形参,什么是实参?

```python
形参: 形式参数,是在函数定义的时候,括号中的变量
实参: 实际参数,是在函数调用的时候,括号是的变量(数据值)
```

### 3. 简述局部变量的特点?

```Python
局部变量: 在函数内部定义的变量.
特点: 只能在函数内部访问
    可以在不同的函数中定义名字相同的局部变量
```

### 4. 简述全局变量的特点?

```Python
全局变量: 在函数外部定义的变量或者使用 global 声明的变量
特点: 全局变量可以在任意函数中的访问
    在函数内部想要修改全局变量的值,需要使用 global 声明
```

### 5. 简述函数中 return 的作用?

```python
return 的作用:
1. 返回一个数据值
2. 终止函数的执行
```

### 6. python中可变类型数据有哪些？不可变类型数据有哪些?

```python
不可变类型: 指内存中的数据不能修改
    数字类型: int  float bool
    字符串: str
    元组: tuple
可变类型: 值内存中的数据可以修改
    列表: list
    字典: dict
```

### 7. 局部变量和全局变量

有如下代码：

```python
num = 10  # 全局变量
def anum():
    num = 20   # 局部变量
    
print(num)   # 函数外部访问打印, 全剧变量
```

请问这段代码最终输出的值是多少？

```python
10
```

### 8. 想要返回多个数据值,应该怎么操作?

```python
组成元组进行返回
```

### 9.如何交换两个变量的值?

```python 
a,b = b, a
```



## 代码

### 题目 1

定义一个函数my_max，包含两个参数, 函数的作用是将两个数据中比较大的数进行返回. 如 10 和 20 , 返回 20.

```Python
# 函数定义
def my_max(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2
```

### 题目 2

定义一个函数 my_sum 接收一个参数 n ，在函数中计算 1 + 2 + 3 + ... + n 的值，并在函数中打印求和结果

```python
def my_sum(n):
    i = 1  # 定义计数器
    num = 0  # 定义变量保存求和的结果
    while i <= n:
        num += i
        i += 1
        print('求和的结果为', num)


sum_test(100)


def my_sum(n):
    num = 0
    for i in range(1, n+1):
        num += i
    print('求和的结果为', num)
```

### 题目3

定义一个函数func, 函数的功能如下:

1. 函数存在两个参数, 可以接收 姓名和 性别两个信息
2. 调用, 如果传递性别信息, 则使用 传递的数据值
3. 如果不传递性别信息, 性别的值为 '保密'
4. 在函数内部打印 姓名和性别信息

```python
def func(name, sex='保密'):
     print(f"姓名: {name}, 年龄: {sex}")

```

### 题目 4

定义一个函数 login, 函数接收两个参数,用户名 `username` 和 密码`password`

函数功能如下:

判断输入的用户名是否是 `admin`, 密码是否是 `123456`, 如果是 输出 `登录成功`如果不是 输出`用户名或密码错误,登录失败`

```python
def login(username, password):
    if username == 'admin' and password == '123456':
        print('登录成功')
    else:
        print('用户名或密码错误登录失败')


user = input('请输入用户名')
word = input('请输入密码')
login(user, word)
```

### 题目 5

定义一个函数 `my_sum`, 函数的功能是 可以对任意多个数字进行求和计算.

```python
def my_sum(*args):   # args 是 元组类型
    # 定义变量, 来保存求和的结果
    num = 0
    for i in args:  # i 是元组中每个数据
        num += i

    print(num)


my_sum()  # 0
my_sum(1)  # 1
my_sum(1, 2)  # 3
my_sum(1, 2, 3)  # 6


def my_sum(*args):
    num = sum(args)
    return num
```

