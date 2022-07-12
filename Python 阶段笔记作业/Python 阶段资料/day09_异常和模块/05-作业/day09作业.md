## day09 作业

## 题目 1

1. 定义一个模块 `calc.py`, 在模块中定义一个函数 `add()`, 函数的作用是求两个数的和

2. 重新定义一个代码文件,在这个代码文件中 使用 `calc.py` 文件中的 `add` 函数 对 两个数字进行求和运算

```Python

```





## 题目 2

1. 定义 `tools.py`, 在文件中定义一个 动物类, 具有实例属性 name 和 age, 类属性class_name,类属性值为  `动物类` 和 play 的方法, 在方法中输出 `快乐的玩耍`
2. 新建一个代码文件, 定义一个 猫类, 继承 动物类,  在 play 方法中 添加以下输出`玩累了,等待铲屎官的投喂中....`

```python

```



## 题目 3

```python
1. 定义 TestCase文件 case1.py, 在文件中 定义一个测试类 TestDemo1, 在测试类中 定义两个测试方法, 直接输出打印一句话即可

2. 直接运行 case1.py, 查看结果

3. 定义 TestCase文件 case2.py, 在文件中 定义一个测试类 TestDemo2, 在测试类中 定义两个测试方法, 直接输出打印一句话即可

4. 直接运行 case2.py, 查看结果

5. 使用 TestSuite 和 TestRunner 将 case1.py 和 case2.py 进行组装,运行
```

## 题目4 

```yacas 
完成对 login 函数的测试
```

```python
# 假设对某网站的登录进行测试
def login(username, password):
    if username == 'admin' and password == '123456':
        return '登录成功'
    else:
        return '登录失败'
    
# 1. 这个是开发书写的代码功能,不要修改我的 login 函数
# 2. 可以认为这函数就是 tpshop 登录

设计测试数据:
正确的用户名和密码: admin,123456, 登录成功
错误的用户名: root, 123456, 登录失败
错误的密码: admin, 123123, 登录失败
错误的用户名和错误的密码: aaa, 123123, 登录失败
```

