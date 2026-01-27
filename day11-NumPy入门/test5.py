import numpy as np
#高级索引
#整数数组索引
x = np.array([[1,  2],  [3,  4],  [5,  6]])
y=x[[0,1,2],[0,1,0]]
print(y)

print()
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print(x)
rows=np.array([[0,0],[3,3]])
cols=np.array([[0,2],[0,2]])
y=x[rows,cols]
print(y)

#借助切片 : 或 … 与索引数组组合
print()
a = np.array([[1,2,3], [4,5,6],[7,8,9]])
b=a[1:3,1:3]
c=a[1:3,[1,2]]
d=a[...,1:]
print(b)
print(c)
print(d)

#布尔索引
print()
x = np.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])
print(x[x>5])
a = np.array([np.nan,  1,2,np.nan,3,4,5])
print (a[~np.isnan(a)])
a = np.array([1,  2+6j,  5,  3.5+5j])
print (a[np.iscomplex(a)])

#花式索引
print()
x=np.arange(9)
x2=x[[0,6]]
print(x2)
print(x2[0])
print(x2[1])

x=np.arange(32).reshape((8,4))
print(x)
#传入顺序索引数组
print (x[[4,2,1,7]])
#传入倒序索引数组
print (x[[-4,-2,-1,-7]])
#传入多个索引数组 np.ix_输入两个数组，产生笛卡尔积的映射关系
print (x[np.ix_([1,5,7,2],[0,3,1,2])])
