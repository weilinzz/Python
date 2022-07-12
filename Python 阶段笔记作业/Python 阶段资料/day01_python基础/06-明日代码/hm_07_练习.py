# 1. 获取用户输入的用户名  --> input
username = input('请输入用户名:')
# 2. 判断用户名是 admin 时, 在控制台输出: 欢迎系统管理员 admin 登录!
if username == 'admin':
    print('欢迎系统管理员 admin 登录!')
# 3. 用户名是 test 时, 在控制台输出: 欢迎测试工程师 test 登录!
elif username == 'test':
    print('欢迎测试工程师 test 登录!')
# 4. 如果是其他信息, 在控制台输出: 查无此人!
else:
    print('查无此人!')
