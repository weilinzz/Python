import json

with open('info3.json', encoding='utf-8') as f:
    info_list = json.load(f)
    # print(info_list[0].get('name'), info_list[0].get('age'))
    # print(info_list[1].get('name'), info_list[1].get('age'))
    for info in info_list:
        print(info.get('username'), info.get('password'))
