# python 切片
# >>> s = 'bicycle'
# >>>s[::3]
# 'bye'
# >>>s[::-1]
# 'elcycib'
# >>>s[::-2]
# 'eccb'
#
# >>> deck[12::13]
# [Card(rank="A",suit="spades"),Card(rank="A",suit="diamonds"),Card(rank="A",suit="clubs"),Card(rank="A",suit="hearts")]
#
# a:b:c 这种用法只能作为索引或者下标用[]中来返回一个切片对象：slice(a,b,c)

import numpy  # 这个不是python的标准库，是一个外部库，需要pip下载安装

a = numpy.arange(12)  # 新建一个0~11的整数的numpy.ndarray,然后把他打印出来
print(a)  # >>> array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])
print(type(a))  # >>> <class 'numpy.ndarray'>
# 看看数组的维度，它是一个一维的，有12个元素的数组
print(a.shape)  # >>> (12,)
# 把数组变成二维的，然后打印出来
a.shape = 3, 4
print(a)  # >>> array([[ 0,  1,  2,  3],[ 4,  5,  6,  7],[ 8,  9, 10, 11]])
# 打印第二行
print(a[2])  # >>> array([ 8,  9, 10, 11])
# 取出第二行第一个元素
print(a[2, 1])  # >>> 9
# 把第一列打印出来
print(a[:, 1])  # >>> array([1,5,9])
# 把行和列交换，就得到一个新数组
print(a.transpose())  # >>>array([[ 0,  4,  8],[ 1,  5,  9],[ 2,  6, 10],[ 3,  7, 11]])
#
# import numpy
#
# floats = numpy.loadtxt('floats-10M-lines.txt')
# floats[-3:]
# floats *= .5


l = list(range(10))
print(l)  # >>>[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[2:5] = [20, 30]
print(l)  # >>> [0, 1, 20, 30, 5, 6, 7, 8, 9]
del l[5:7]
print(l)  # >>> [0, 1, 20, 30, 5, 8, 9]
l[3::2] = [11, 22]
print(l)  # >>>[0, 1, 20, 11, 5, 22, 9]
# 如果赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象，即便只有单独的一个值，也要把他转换为可迭代的序列
# l[2:5] = 100  # >>> TypeError: can only assign an iterable
l[2:5] = [100]
print(l)  # >>> [0, 1, 100, 22, 9]
c = [i for i in range(10) if i > 0]
print(c)



