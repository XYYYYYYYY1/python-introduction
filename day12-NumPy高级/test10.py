import numpy as np
#副本和视图
#无复制
a = np.arange(6)
print(a)
print(id(a))
b=a
print(b)
print(id(b))
b.shape=3,2
print(b)
print(a)

#视图或浅拷贝
print()
a = np.arange(6).reshape(3,2)
print(a)
b=a.view()
print(b)
print(id(a))
print(id(b))
b.shape=2,3
print(b)
print(a)

#使用切片创建视图修改数据会影响到原始数组
print()
arr = np.arange(12)
print(arr)
a=arr[3:]
b=arr[3:]
a[1]=123
b[2]=234
print(arr)

#副本或深拷贝
print()
a = np.array([[10,10],  [2,3],  [4,5]])
print(a)
b=a.copy()
print(b)
print(b is a)
b[0,0]=100
print(b)
print(a)
