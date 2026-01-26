#从已有的数组创建数组 numpy.asarray
import numpy as np
#将列表转化为ndarray
x=[1,2,3]
a=np.asarray(x,dtype=float)
print(x)
print(a)

#将元组转化为ndarray
print()
x=(1,2,3)
a=np.asarray(x)
print(x)
print(a)

#将元组列表转化为ndarray
print()
x=[(1,2,3),(4,5,6)]
a=np.asarray(x)
print(x)
print(a)

#numpy.frombuffer 用于实现动态数组
print()
s=b'Hello World'
a=np.frombuffer(s,dtype='S1')
print(a)

#numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组
print()
list=range(5)
it=iter(list)
x=np.fromiter(it,dtype=float)
print(x)

#从数值范围创建数组
print()
x=np.arange(5,dtype=float)
print(x)

x=np.arange(10,20,2)
print(x)

#numpy.linspace 函数用于创建一个等差数列
a=np.linspace(1,10,10)
print(a)

#numpy.logspace 函数用于创建一个等比数列
a=np.logspace(1.0,2.0,num=10)
print(a)
a = np.logspace(0,9,10,base=2)
print (a)