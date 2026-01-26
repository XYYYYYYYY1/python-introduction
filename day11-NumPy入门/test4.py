import numpy as np
#切片和索引
a=np.arange(10)
s=slice(2,7,2)
print(a)
print(a[s])
b=a[2:7:2]
print(b)
b=a[5]
print(b)
print(a[2:])
print(a[2:5])

#多维数组
print()
a=np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
print(a[1:])
print(a[...,1])
print(a[1,...])
print(a[...,1: ])