#  可以使用 read 方法读取, 得到的字符串,处理起来很麻烦, json 文件的读取不使用 read

# 1. 导包
import json

# 2. 打开文件
with open('info.json', 'r', encoding='utf-8') as f:
    # 3. json.load(文件对象)  --> 得到 列表或者字典
    result = json.load(f)
    print(type(result))
    # 名字
    print(result.get('name'))
    print(result.get('age'))
    print(result.get('address').get('city'))

