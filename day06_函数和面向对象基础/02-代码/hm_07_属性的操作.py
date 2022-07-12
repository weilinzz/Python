

class Cat:
    def __init__(self):
        self.name = "烂面"
        self.age =2
        print(f'{id(self)},self')
        print(f'小米{self.name} {self.age}爱吃鱼.....')
        print(f'小猫{self.name} {self.age}爱吃鱼...')
    def show_info(self):
        print(f'小猫的名字是: {self.name}, 年龄是: {self.age}')
blue_cat=Cat()
blue_cat.show_info()


