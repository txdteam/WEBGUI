from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):  # 定义输出表示方法
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)  # 求向量的模

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):  # 定义+方法
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, other):  # 定义 * 方法
        return Vector(self.x * other, self.y * other)

    def __str__(self):
        return "这是一个特殊函数方法"


v1 = Vector(2, 4)
v2 = Vector(2, 1)

print(v1 + v2)
# v = Vector(3, 4)
# print(abs(v))
# print(abs(v * 3))
# # print(Vector())
# a = "ss"
# c = str.format(a)
# print(c)
# print('我叫%s，今年%s岁。' % ('小明', 18))
