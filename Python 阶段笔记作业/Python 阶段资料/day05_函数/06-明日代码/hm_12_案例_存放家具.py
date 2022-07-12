# 定义家具类
class HouseItem:
    def __init__(self, name, area):
        self.name = name  # 名字
        self.area = area  # 占地面积

    def __str__(self):
        return f"家具{self.name}占地面积{self.area} 平米"


# 定义房子类
class House:
    def __init__(self, name, area):
        self.name = name  # 户型
        self.area = area  # 总面积
        self.free_area = area  # 初始面积和剩余面积是相等的
        self.item_list = []  # 因为没有家具,所以是空列表

    def __str__(self):
        return f"户型:{self.name}, 总面积:{self.area}, 剩余面积:{self.free_area}, " \
               f"家具名称列表: {self.item_list}"

    def add_item(self, item):  # item 参数是要添加的家具对象
        # 添加家具,在房子对象(self)添加家具对象(item)
        # 1. 判断房子的剩余面积(self.free_area)和家具的占地面积(item.area)的关系
        if self.free_area > item.area:
            # 添加家具, 将家具的名字添加到房子中的家具名称列表中
            self.item_list.append(item.name)
            # 修改剩余面积  剩余面积(self.free_area) = 当前的剩余面积(self.free_area) - 家具的占地面积(item.area)
            self.free_area -= item.area
            print(f"家具 {item.name} 添加成功")
        else:
            print('剩余面积不足,添加失败, 换个大房子吧')


# 创建家具类的对象
bed = HouseItem('席梦思', 4)
print(bed)
chest = HouseItem('衣柜', 2)
print(chest)
table = HouseItem('餐桌', 1.5)
print(table)

# 创建房子对象
house = House('三室一厅', 150)
print(house)
house.add_item(bed)
print(house)
house.add_item(bed)
print(house)
