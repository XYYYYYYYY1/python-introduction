import numpy as np
#numpy.empty 方法用来创建一个指定形状（shape）、数据类型（dtype）且未初始化的数组
x=np.empty([3,2],dtype=int)
print(x)

#numpy.zeros 创建指定大小的数组，数组元素以 0 来填充
print()
#默认为浮点数
x=np.zeros(5)
print(x)
#设置为整数
y=np.zeros(5,dtype=int)
print(y)
#自定义类型
z=np.zeros((2,2),dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

#numpy.ones 创建指定形状的数组，数组元素以 1 来填充
#默认为浮点数
print()
x=np.ones(5)
print(x)
y=np.ones((2,2),dtype=int)
print(y)

#numpy.zeros_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 0 来填充
print()
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
zeros_arr=np.zeros_like(arr)
print(zeros_arr)

#numpy.ones_like 用于创建一个与给定数组具有相同形状的数组，数组元素以 1 来填充
print()
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ones_arr=np.ones_like(arr)
print(ones_arr)