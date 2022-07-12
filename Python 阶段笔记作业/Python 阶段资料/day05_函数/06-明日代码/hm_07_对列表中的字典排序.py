user_list = [
    {"name": "zhangsan", "age": 18, 'height': 190},
    {"name": "lisi", "age": 19, 'height': 185},
    {"name": "wangwu", "age": 17, 'height': 183}
]
# 列表排序使用的 sort

# user_list.sort()
# 排序: 默认是对列表中数据进行比大小操作的,如果列表中数据是数字(可以直接比大小), 但是如果是字典,不能直接比大小
# sort()函数不知道怎么比较字典的大小, 目前的需求,就是要对列表中的字典进行排序,此时,需要我们告诉 sort 函数,我们
# 对列表中的字典按照什么规则(数据)进行排序, (我们定义一个函数,取出字典中的某个键对应的值,把这个函数作为参数传递给
# sort 函数, 这个函数一般使用 匿名函数)
# sort() 函数中 key 参数就是用来接收 传递的函数的

# 按照 年龄排序, 定义一个函数,将 年龄对应的值返回 lambda x: x['age']
user_list.sort(key=lambda x: x['age'])
print(user_list)
# 按照年龄降序
user_list.sort(key=lambda x: x['age'], reverse=True)
print(user_list)
# 按照 身高排序, 定义一个函数,将 身高对应的值返回 lambda x: x['height']
user_list.sort(key=lambda x: x['height'])
print(user_list)

# 结论: 对列表装字典按照某个键排序的代码
# 列表.sort(key=lambda x: x['键'])  # x 是形参,可以是任意的变量名,在 sort 函数内部调用的时候, x 是列表中数据(字典)

