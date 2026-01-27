import numpy as np
#迭代数组
a=np.arange(6).reshape(2,3)
print(a)
print(a.T)
for x in np.nditer(a):
    print(x,end=",")
print()
#通过显式设置，来强制 nditer 对象使用某种顺序
for x in np.nditer(a,order='F'):
    print(x,end=",")
print()
for x in np.nditer(a.T):
    print(x,end=",")
print()
for x in np.nditer(a.T.copy(order='C')):
    print(x,end=",")
print()

#修改数组中元素的值
print()
a=np.arange(0,60,5).reshape(3,4)
print(a)
for x in np.nditer(a,op_flags=['readwrite']):
    x[...]=2*x
print(a)

#使用外部循环
print()
a=np.arange(0,60,5).reshape(3,4)
for x in np.nditer(a,flags=['external_loop'],order='C'):
    print(x,end=",")
print()

#广播迭代
print()
a=np.arange(0,60,5).reshape(3,4)
b = np.array([1,  2,  3,  4], dtype =  int)
print(a)
print(b)
for x,y in np.nditer([a,b]):
    print("%d:%d" %(x,y),end=",")