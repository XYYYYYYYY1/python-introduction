#安装matplotlib python3 -m pip install -U matplotlib
import matplotlib.pyplot as plt
import numpy as np
#Matplotlib Pyplot
xpoints=np.array([0,6])
ypoints=np.array([0,100])

plt.plot(xpoints,ypoints)
plt.show()

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints,ypoints)
plt.show()

#如果我们只想绘制两个坐标点，而不是一条线，可以使用 o 参数，表示一个实心圈的标记
plt.plot(xpoints,ypoints,'o')
plt.show()

xpoints=np.array([1,2,6,8])
ypoints=np.array([3,8,1,10])

plt.plot(xpoints,ypoints)
plt.show()

#如果我们不指定 x 轴上的点，则 x 会根据 y 的值来设置为 0, 1, 2, 3..N-1
ypoints = np.array([3, 10])

plt.plot(ypoints)
plt.show()

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()

x = np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)
plt.plot(x,y,x,z)
plt.show()