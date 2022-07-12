# 无参无返回值  打印输出 hello world
def func1():
    print('hello world')


func1()
# lambda : print('hello world')
func11 = lambda: print('hello lambda')
func11()


# 无参有返回值  返回 100
def func2():
    return 100


print(func2())
func22 = lambda: 200
print(func22())


# 有参无返回值,  将参数进行打印
def func3(info):
    print(info)


func3('hello')
func33 = lambda info: print(info)
func33('你好')
# 有参有返回值[使用较多]  求两个数的和
def func4(a, b):
    return a + b


print(func4(10, 20))
func44 = lambda x, y: x + y
print(func44(1, 2))
