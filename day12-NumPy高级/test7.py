import numpy as np
#统计函数
#numpy.amin() 用于计算数组中的元素沿指定轴的最小值  numpy.amax() 用于计算数组中的元素沿指定轴的最大值
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(a)
print(np.amin(a,1))
print(np.amin(a,0))
print (np.amax(a))
print (np.amax(a,axis=0))
#numpy.ptp() 函数计算数组中元素最大值与最小值的差
print()
a = np.array([[3,7,5],[8,4,3],[2,4,9]])
print(np.ptp(a))
print(np.ptp(a,axis=1))
print(np.ptp(a,0))
#百分位数是统计中使用的度量，表示小于这个值的观察值的百分比
print()
a = np.array([[10, 7, 4], [3, 2, 1]])
print(a)
# 50% 的分位数，就是 a 里排序之后的中位数
print(np.percentile(a, 50))
# axis 为 0，在纵列上求
print(np.percentile(a, 50, axis=0))
# axis 为 1，在横行上求
print(np.percentile(a, 50, axis=1))
# 保持维度不变
print(np.percentile(a, 50, axis=1, keepdims=True))
#numpy.median() 函数用于计算数组 a 中元素的中位数
print()
a = np.array([[30,65,70],[80,95,10],[50,90,60]])
print(a)
print (np.median(a))
print (np.median(a,axis=0))
print (np.median(a,axis=1))
#numpy.mean() 函数返回数组中元素的算术平均值，如果提供了轴，则沿其计算
print()
a = np.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
print (np.mean(a))
print (np.mean(a, axis =  0))
print (np.mean(a, axis =  1))
#numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
print()
a = np.array([1,2,3,4])
print (np.average(a))
wts = np.array([4,3,2,1])
print(np.average(a,weights=wts))
print (np.average([1,2,3,4],weights=[4,3,2,1], returned =  True))
#多维数组
print()
a = np.arange(6).reshape(3,2)
print(a)
wt = np.array([3,5])
print (np.average(a, axis =  1, weights = wt))
#标准差、方差
print()
print (np.std([1,2,3,4]))
print (np.var([1,2,3,4]))