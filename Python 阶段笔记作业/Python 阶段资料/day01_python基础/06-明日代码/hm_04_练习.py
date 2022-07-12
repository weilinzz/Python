# 1. 获取用户输入的用户名信息
# name = input('请输入你的用户名:')   # str
# # 2. 如果用户名信息是 admin, 就在控制台输出出来
# if name == 'admin':
#     print(f"用户名是{name}")
# else:
#     # 3. 如果用户名信息不是 admin, 就在控制台输出"用户名错误!"
#     print('用户名错误!')


# # 1. 获取用户输入的用户名和密码 -- > input
# username = input('请输入用户名:')  # str
# password = input('请输入密码:')  # str
# # 2. 判断用户名是 admin 并且密码是 123456 时, 在控制台输出: 登录成功!
# if username == 'admin' and password == '123456':
#     print('登录成功! ')
# else:
#     # 3. 否则在控制台输出: 登录信息错误!
#     print('登录信息错误!')


# 1. 获取用户输入的用户名
username = input('请输入用户名:')  # str

# 2. 判断用户名是 admin 时, 在控制台输出: 欢迎 admin 登录!
# 3. 用户名是 test 时, 在控制台输出: 欢迎 test 登录!
if username == 'admin' or username == 'test':
    print(f"欢迎 {username} 登录!")
else:
    # 4. 如果是其他信息, 在控制台输出: 查无此人!
    print('查无此人!')


