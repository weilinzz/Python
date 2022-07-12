## day03 作业题

## 简答题

### 1. 写出 for 循环的基本格式

```python
for 变量 in  容器:
    重复执行的代码
    
for 变量 in range(n):
    pass

for 变量 in range(start, end):
    pass

```

### 2. 简述 break 和 continue 的作用

```python
break和 continue 只能用在循环中
break 终止循环的执行
continue 是结束本次循环,继续下一次循环
```

### 3. 简述字符串查找和替换方法的使用

```python
字符串.find(sub_str, start, end)  在字符串从查找 sub_str
# sub_str 要查找的内容
# start 开始位置的下标, 即从什么位置开始查找, 默认是 0
# end 结束位置的下标,到什么地方查找结束, 
# 返回值: 方法执行的结果,找到 sub_str ,返回 sub_str 开始的下标, 没有找到,返回-1

字符串.replace(old_str, new_str, count)  字符串的替换, 不会修改原字符串的内容, 会得到一个新的字符串
# old_str 原字符串
# new_str 新字符串
# count 替换的次数,默认是全部替换
# 返回: 替换之后新的字符串
```

### 4. 简述字符串拆分和连接方法的使用

```python 
字符串.split(sep, maxsplit) 将字符串按照 sep 进行切割(分隔)
# sep 分隔符,即字符串按照什么进行分隔, 默认是空白字符(空格 \n \t)
# maxsplit 分隔的次数
# 返回值: 列表,列表中数据是分隔好的字符串

字符串.join(列表)  # 可以是字符串,可以元组, 可以是字典等
# 将字符串添加到列表中每两个元素之间
# 返回值: 得到一个字符串
# 注意点: 列表中的元素必须都是字符串类型
```




## 代码题

### 题目1 字符串下标练习

```python
# 定义字符串 abcdefgh
my_str = 'abcdefgh'
# 打印输出下标为 3 的字符
print(my_str[3])
# 打印输出字符串中第二个字符
print(my_str[1])
# 打印输出字符串中最后一个数据
print(my_str[-1])
# 打印输出字符串中倒数第二个数据
print(my_str[-2])
# 打印输出字符串的长度(元素的个数)
print(len(my_str))
```



### 题目 2 使用字符串切片完成以下练习

```python
#  现在有字符串：
msg = "ABCDEFGHIJ"
# 	1. 截取下标为2 ~ 5(包含) 字符 的字符
msg1 = msg[2:6]
# 	2. 截取从 2 ~ 末尾(包含) 的字符串
msg2 = msg[2:]
# 	3. 截取从 开始 ~ 5(包含) 字符 的字符串
msg3 = msg[:6]
msg3 = msg[0:6]
# 	4. 截取从 2 ~ 末尾(不包含) 的字符串
msg4 = msg[2:-1]
# 	5. 截取字符串末尾两个字符
msg5 = msg[-2:]
# 	6. 字符串的逆序(逆置)
msg6 = msg[::-1]
```



### 题目 3 列表的练习

```python 
# 定义一个空列表 list1
list1 = []
list1 = list()
# 定义一个列表 list2 包含以下数据 : 18, '小王', 171.4, True
list2 = [18, '小王', 171.4, True]
# 打印输出 list2 中数据的个数
print(len(list2))
# 打印输出 list2中 第 2 个数据
print(list2[1])
# 打印输出 list2中最后一个数据
print(list2[-1])
```



### 题目 4 字符串常见方法的使用

```python 
# 定义一个字符串 str1, 字符串的内容为 "hello world and itcast and itheima and Python"
str1 = "hello world and itcast and itheima and Python"
# 在字符串str1中查找 字符串 and 的下标
num = str1.find('and')
print(num)
# 在字符串str1中查找字符串 'good'的下标
num1 = str1.find('good')
print(num1)
# 将字符串str1中的 and 替换为 or
str2 = str1.replace('and', 'or')
print(str2)
# 将字符串 str1 按照 空白字符进行切割,保存到变量 list1 中
list1 = str1.split()
print(list1)
# 使用 _*_ 将 list1中的字符串进行连接
str3 = '_*_'.join(list1)
# 使用 逗号 将 list1中的字符串进行连接
str4 = ','.join(list1)
```



### 题目5  列表添加数据

```python
# 1.定义一个空列表my_list
my_list = []
print(my_list)
# 2. 向列表中添加数据 '郭德纲'
my_list.append('郭德纲')
print(my_list)
# 3. 向列表的尾部添加数据 '岳云鹏'
my_list.append('岳云鹏')
print(my_list)
# 4. 向列表的尾部添加数据 '郭麒麟'
my_list.append('郭麒麟')
print(my_list)
# 5. 在下标为1 的位置添加数据 '于谦'
my_list.insert(1, '于谦')
print(my_list)
# 6. 定义一个列表my_list2, 包含数据:  孙越, 张云雷, 张鹤伦
my_list2 = ['孙越', '张云雷', '张鹤伦']
print(my_list)
# 7. 将 my_list2 中的数据逐个添加到my_list 中
my_list.extend(my_list2)
print(my_list)

```



### 题目7 字符串遍历

要求用户输入一个字符串，遍历当前字符串并打印字符，如果遇见字符“q”,则跳出循环。如果遇见“  ”（空格）则跳过不输出。

#### 答案

```python
# 获取用户输入的字符串
input_str = input("请输入一个字符串：")
# 遍历字符串
for i in input_str:
    # 如果是q ,循环终止
    if i == "q":
        break
    elif i == " ":
        # 如果是空格, 跳过输出
        continue
    print(i)
    
    
# 获取用户输入的字符串
input_str = input("请输入一个字符串：")
# 遍历字符串
for i in input_str:
    # 如果是q ,循环终止
    if i == "q":
        break
    elif i == " ":
        # 如果是空格, 跳过输出
        continue
    else:
    	print(i)
```





### 题目 7 过 7 游戏

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
i = 1
while i <= 99:
    if i % 7 == 0 or str(i).find('7') != -1:
        print('过')
    else:
        print(i)

    i += 1
    
    
for j in range(1, 100):
    if j % 7 == 0 or str(j).find('7') != -1:
        print('过')
    else:
        print(j)
        
for j in range(1, 100):
    if j % 7 == 0 or '7' in str(j):
        print('过')
    else:
        print(j)        
```





### 题目8 列表操作

有一个列表，判断列表中的每一个元素是否以s或e结尾，如果是，则将其放入一个新的列表中，最后输出这个新的列表

```python
list1 = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]
```

```yacas
提示: 字符串以什么结尾,即字符串中最后一个字符是 什么.
```

```python
my_list = ["red", "apples", "orange", "pink", "bananas", "blue", "black", "white"]

# 用来存放以e或者s结尾的字符串
new_list = []

for i in my_list:  # i 是列表中的数据(字符串)
    # 判断列表中每一个元素是否以s或e结尾
    if i[-1] == 's' or i[-1] == 'e':
        new_list.append(i)

# 打印出这个新的列表
print(new_list)
```



### 题目 9 随机抽签功能[提高]

```python 
1. 使用 input 输入 5 个学生的名字存入列表
2. 随机的获取一个学生的名字并打印
```

#### 答案

```python
import random
# 定义列表存储所有的学生信息
name_list = []

# 书写循环
for i in range(5):
    name = input('请输入名字:')
    # 将输入的名字存入列表
    name_list.append(name)

# 使用随机数产生列表的的下标
num = random.randint(0, 4)
# 打印抽到的学生
print(name_list[num])
```

### 题目 10  for 循环求 1- 100 之间数字的和

```python
num = 0 
for i in range(1, 101):
    num += i
    
print(num)
```

