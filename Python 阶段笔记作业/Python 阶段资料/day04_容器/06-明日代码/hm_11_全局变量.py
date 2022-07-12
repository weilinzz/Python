# 定义全局变量
g_num = 100


def func1():
    print('func1:', g_num)


def func2():
    g_num = 10  # 局部变量, 只是和全局变量的名字一样
    print("func2:", g_num)   # 10


# 定义一个函数修改全局变量
def func3():
    # 在函数内部想要修改全局变量,需要使用 关键字 global 进行声明
    global g_num
    g_num = 200
    print('func3:', g_num)  # 200


func1()  # func1: 100
func2()  # func2: 10
func3()  # func3: 200
func1()  # func1: 200
func2()  # func2: 10
