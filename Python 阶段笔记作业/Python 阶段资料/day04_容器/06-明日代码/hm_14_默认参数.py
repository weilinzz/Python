# sex 和 age 是缺省默认参数
def show_info(name, age=0, sex='保密'):
    print(f"name:{name}, age:{age}, sex:{sex}")


show_info('小明', 18, '男')
show_info('小王', 18)
show_info('小红')
# 1. 小花  性别  男
show_info('小花', sex='男')


