import numpy as np
#NumPy IO
#numpy.save() 函数将数组保存到以 .npy 为扩展名的文件中
a = np.array([1,2,3,4,5])
# 保存到 outfile.npy 文件上
np.save('outfile.npy', a)
# 保存到 outfile2.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
np.save('outfile2', a)
#使用 load() 函数来读取数据
b=np.load('outfile.npy')
print(b)

#numpy.savez() 函数将多个数组保存到以 npz 为扩展名的文件
print()
a = np.array([[1,2,3],[4,5,6]])
b = np.arange(0, 1.0, 0.1)
c = np.sin(b)
np.savez('mww.npz',a,b,sin_array=c)
r=np.load('mww.npz')
print(r.files)
print(r['arr_0'])
print(r['arr_1'])
print(r['sin_array'])

#savetxt() 函数是以简单的文本文件格式存储数据，对应的使用 loadtxt() 函数来获取数据
print()
a = np.array([1,2,3,4,5])
np.savetxt('out.txt',a)
b=np.loadtxt('out.txt')
print(b)

#使用 delimiter 参数
print()
a=np.arange(0,10,0.5).reshape(4,-1)
np.savetxt('out.txt',a,fmt="%d",delimiter=",")
b=np.loadtxt('out.txt',delimiter=",")
print(b)