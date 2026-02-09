import matplotlib.pyplot as plt
import numpy as np
#Matplotlib 绘图标记
#以使用 plot() 方法的 marker 参数来定义坐标标记
ypoints = np.array([1,3,4,5,8,9,6,1,3,4,5,2,4])

plt.plot(ypoints,marker='o')
plt.show()

#fmt 参数定义了基本格式，如标记、线条样式和颜色
ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints,'o:r')
plt.show()

#标记大小与颜色
plt.plot(ypoints,marker='o',ms=20)
plt.show()

#设置标记外边框颜色
plt.plot(ypoints,marker='o',ms=20,mec='r')
plt.show()

#设置标记内部颜色
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()

#自定义标记内部与边框的颜色
plt.plot(ypoints, marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')
plt.show()