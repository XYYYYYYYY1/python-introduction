import numpy as np
#数组操作
#修改数组形状 numpy.reshape
a=np.arange(8)
b=a.reshape(4,2)
print(a)
print(b)

#numpy.ndarray.flat 是一个数组元素迭代器
print()
a = np.arange(9).reshape(3,3)
for row in a:
    print(row)
for element in a.flat:
    print(element)

#numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
print()
a = np.arange(8).reshape(2,4)
print(a)
print(a.flatten())
print(a.flatten(order='F'))

#numpy.ravel() 展平的数组元素
print()
a = np.arange(8).reshape(2,4)
print(a)
print(a.ravel())

#翻转数组
#numpy.transpose 函数用于对换数组的维度 与ndarray.T类似(转置)
print()
a = np.arange(12).reshape(3,4)
print(a)
print(np.transpose(a))
print(a.T)

#numpy.rollaxis 函数向后滚动特定的轴到一个特定位置
print()
a = np.arange(8).reshape(2,2,2)
print(a)
print(np.where(a==6))
print(a[1,1,0])
#轴2滚动到轴0
b=np.rollaxis(a,2,0)
print(b)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
# 最后一个 0 移动到最前面
print(np.where(b==6))

#numpy.swapaxes 函数用于交换数组的两个轴
print()
a = np.arange(8).reshape(2,2,2)
print(a)
print(np.swapaxes(a,2,0))

#修改数组维度
#numpy.broadcast 用于模仿广播的对象，它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果。
print()
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
# 对 y 广播 x
b=np.broadcast(x,y)
r,c=b.iters
print (next(r), next(c))
print (next(r), next(c))
b=np.broadcast(x,y)
print(b.shape)
c=np.empty(b.shape)
print(c.shape)
c.flat=[u+v for (u,v) in b]
print(c)
print(x+y)

#numpy.broadcast_to 函数将数组广播到新形状。
print()
a = np.arange(4).reshape(1,4)
print(a)
print(np.broadcast_to(a,(4,4)))

#numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状
print()
x = np.array(([1,2],[3,4]))
print(x)
y=np.expand_dims(x,axis=0)
print(y)
print(x.shape,y.shape)
y=np.expand_dims(x,axis=1)
print(y)
print (x.ndim,y.ndim)
print (x.shape, y.shape)

#numpy.squeeze 函数从给定数组的形状中删除一维的条目
print()
x = np.arange(9).reshape(1,3,3)
print (x)
y = np.squeeze(x)
print (y)
print (x.shape, y.shape)

#连接数组
#numpy.concatenate 函数用于沿指定轴连接相同形状的两个或多个数组
#numpy.stack 函数用于沿新轴连接数组序列
#numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组
#numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组。
print()
a = np.array([[1,2],[3,4]])
print (a)
b = np.array([[5,6],[7,8]])
print (b)
print(np.concatenate((a,b)))
print (np.concatenate((a,b),axis = 1))
print(np.stack((a,b),0))
print(np.stack((a,b),1))
c = np.hstack((a,b))
print (c)
c = np.vstack((a,b))
print (c)

#分割数组
#numpy.split 函数沿特定的轴将数组分割为子数组
print()
a = np.arange(9)
b=np.split(a,3)
print(b)
b=np.split(a,[4,7])
print(b)
#numpy.hsplit 函数用于水平分割数组
print()
harr = np.floor(10 * np.random.random((2, 6)))
print(harr)
print(np.hsplit(harr,3))
#numpy.vsplit 沿着垂直轴分割
print()
a = np.arange(16).reshape(4,4)
b = np.vsplit(a,2)
print (b)

#数组元素的添加与删除
#numpy.resize 函数返回指定大小的新数组。
print()
a = np.array([[1,2,3],[4,5,6]])
print(a)
b=np.resize(a,(3,2))
print(b)
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了
b = np.resize(a,(3,3))
print (b)
#numpy.append 函数在数组的末尾添加值。
print(np.append(a,[7,8,9]))
print (np.append(a, [[7,8,9]],axis = 0))
print (np.append(a, [[5,5,5],[7,8,9]],axis = 1))
#numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值。
print()
a = np.array([[1,2],[3,4],[5,6]])
print(a)
print(np.insert(a,3,[11,12]))
print ('沿轴 0 广播：')
print (np.insert(a,1,[11],axis = 0))
print ('沿轴 1 广播：')
print (np.insert(a,1,11,axis = 1))
#numpy.delete 函数返回从输入数组中删除指定子数组的新数组。
print()
a = np.arange(12).reshape(3, 4)
print(a)
print(np.delete(a,5))
print (np.delete(a,1,axis = 1))
#numpy.unique 函数用于去除数组中的重复元素。
print()
a = np.array([5,2,6,2,7,5,6,8,2,9])
print(a)
print ('第一个数组的去重值：')
u=np.unique(a)
print(u)
print ('去重数组的索引数组：')
u,indices=np.unique(a,return_index=True)
print(indices)
print ('我们可以看到每个和原数组下标对应的数值：')
print (a)
print ('去重数组的下标：')
u,indices = np.unique(a,return_inverse = True)
print (u)
print (indices)
print ('使用下标重构原数组：')
print (u[indices])
print ('返回去重元素的重复数量：')
u,indices = np.unique(a,return_counts = True)
print (u)
print (indices)