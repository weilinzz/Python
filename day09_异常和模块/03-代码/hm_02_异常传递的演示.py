def func1():
    num = 10 / 0
    print(num)


def func2():
    print('1111')
    func1()


try:
    func2()
except Exception as e:
    print(e)

