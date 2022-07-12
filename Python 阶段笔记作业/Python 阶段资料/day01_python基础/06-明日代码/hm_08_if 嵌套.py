# 假定密码: 147258, 余额: 1000
password = '147258'
money = 1000
# 1. 获取用户输入的密码
pw = input('请输入你的银行卡密码:')
# 2. 判断密码是否正确, 如果正确,获取要取款的金额,
if pw == password:
    print('密码正确')
    # 获取要取款的金额,
    input_money = int(input('请输入要取款的金额:'))
    # 4. 取款时需要判断取款的金额和账户余额的关系
    if money >= input_money:
        print('取款成功')
    else:
        print('余额不足')
# 3. 如果不正确,提示 密码错误,重新输入
else:
    print('密码错误,重新输入')
