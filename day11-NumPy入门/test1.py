#NumPy 安装  pip3 install numpy
import numpy as np
#Ndarray对象
a=np.array([1,2,3])
print(a)

a=np.array([[1,2],[3,4]])
print(a)

a=np.array([1,2,3,4],ndmin=2)
print(a)

a=np.array([1,2,3],dtype=complex)
print(a)

#数组类型
print()
dt=np.dtype(np.int32)
print(dt)

dt=np.dtype('i4')
print(dt)

dt=np.dtype('<i4')
print(dt)

dt=np.dtype([('age',np.int8)])
print(dt)
a=np.array([(10.),(20,),(30,)],dtype=dt)
print(a)
print(a['age'])

student=np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(student)
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)
print(a['age'])

#数组属性
#ndarray.ndim 用于获取数组的维度数量
a=np.arange(24)
print(a)
print(a.ndim)
b=a.reshape(2,4,3)
print(b)
print(b.ndim)

#ndarray.shape 表示数组的维度，返回一个元组，这个元组的长度就是维度的数目
print()
a=np.array([[1,2,3],[4,5,6]])
print(a.shape)
#shape调整数组大小
a.shape=(3,2)
print(a)
#reshape调整数组大小
b=a.reshape(3,2)
print(b)

#ndarray.itemsize 以字节的形式返回数组中每一个元素的大小
print()
x=np.array([1,2,3,4,5],dtype=np.int8)
print(x.itemsize)
y=np.array([1,2,3,4,5],dtype=np.float64)
print(y.itemsize)

#ndarray.flags 返回 ndarray 对象的内存信息
print()
x=np.array([1,2,3,4,5])
print(x.flags)