def func1():
    print('1')
    print('func1')
    print('2')


def func2():
    print('3')
    func1()  # 调用 func1
    print('4')


print('5')
func2()
print('6')
# 531246

