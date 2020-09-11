import os

x, y = (2, 10)  # 这里是元组拆包
print(x, y)
x, y = y, x  # 这里是优雅的交换变量值
print(x, y)
print(divmod(20, 1))
t = (39, 3)
for i in t:
    print(i)
print(divmod(*t))  # * 可以把一个可以迭代的对象拆开作为参数
x, y = divmod(*t)
print(x, y)

_, s = os.path.split("/home")  # 这个函数会返回以路径和最后一个文件组成的元组
print(s)  # s = home

a, b, *rest = range(5)
print(a)  # a = 0
print(b)  # b = 1
print(rest)  # rest = [2,3,4]
a, b, *rest = range(3)
print(a)  # a = 0
print(b)  # b = 1
print(rest)  # rest = [2]
a, b, *rest = range(2)
print(a)  # a = 0
print(b)  # b = 1
print(rest)  # rest = []
