def func():
    a = 10  # a 就是局部变量,只能在函数内部使用
    print(a)


def func2():
    a = 100
    print(a)


func()  # 10
func2()  # 100
func()   # 10



