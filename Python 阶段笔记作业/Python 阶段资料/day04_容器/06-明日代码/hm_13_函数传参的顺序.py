def func(a, b, c):
    print(f"a:{a}, b:{b}, c:{c}")


# 位置传参, 按照位置顺序,将 1 2 3 给到形参 a b c
func(1, 2, 3)  # a:1, b:2, c:3

# 关键字传参, 指定将实参给到哪个形参,顺序无所谓, 形参的名字需要存在
func(b=1, a=3, c=2)  # a:3, b:1, c:2

# 混合使用
func(1, 2, c=3)  # a:1, b:2, c:3

# 列表.sort(reverse=True)
