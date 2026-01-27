import numpy as np
#线性代数
#numpy.dot() 对于两个一维的数组，计算的是这两个数组对应下标元素的乘积和
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.dot(a,b))

#numpy.vdot() 函数是两个向量的点积
print()
a = np.array([[1,2],[3,4]])
b = np.array([[11,12],[13,14]])
print(np.vdot(a,b))

#numpy.inner() 函数返回一维数组的向量内积
print()
print(np.inner(np.array([1,2,3]),np.array([0,1,0])))
#多维数组返回最后一个轴上的和的乘积
a = np.array([[1,2], [3,4]])
b = np.array([[11, 12], [13, 14]])
print(np.inner(a,b))

#numpy.matmul 函数返回两个数组的矩阵乘积
print()
a = [[1,0],[0,1]]
b = [[4,1],[2,2]]
print (np.matmul(a,b))
#维度大于二的数组
a = np.arange(8).reshape(2,2,2)
b = np.arange(4).reshape(2,2)
print (np.matmul(a,b))

#numpy.linalg.det() 函数计算输入矩阵的行列式
print()
a = np.array([[1,2], [3,4]])
print(np.linalg.det(a))
b = np.array([[6,1,1], [4, -2, 5], [2,8,7]])
print (b)
print (np.linalg.det(b))

#numpy.linalg.solve() 函数给出了矩阵形式的线性方程的解
#numpy.linalg.inv() 函数计算矩阵的乘法逆矩阵
print()
x = np.array([[1,2],[3,4]])
print(x)
y=np.linalg.inv(x)
print(y)
print(np.dot(x,y))

print()
a = np.array([[1,1,1],[0,2,5],[2,5,-1]])
print(a)
ainv=np.linalg.inv(a)
print(ainv)
b = np.array([[6],[-4],[27]])
print (b)
x=np.linalg.solve(a,b)
#结果也可以使用该函数获取: x = np.dot(ainv,b)
print(x)