def func(list1):
    list1.append(10)


my_list = [1, 2]
func(my_list)
print(my_list)
# ① [1, 2]  ② [1, 2, 10]


def func(list1):
    list1[0] = 10


my_list = [1, 2]
func(my_list)
print(my_list)

# ① [1, 2]  ②[10, 2]