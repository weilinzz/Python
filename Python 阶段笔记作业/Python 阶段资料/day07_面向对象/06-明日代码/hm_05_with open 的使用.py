import random


with open('c.txt', 'a', encoding='utf-8') as f:
    num = random.randint(1, 100)  #  int
    # f.write(str(num))  # write() 必须是字符串
    f.write(f"{num} ")


# 读
with open('c.txt', encoding='utf-8') as f:
    data = f.read()
    print(data)   # data 字符串,
    # 将字符串转换为列表
    my_list = data.split()
    print(my_list[1])