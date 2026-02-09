import matplotlib.pyplot as plt
import numpy as np
#Matplotlib 绘图线
#线的类型可以使用 linestyle 参数来定义，简写为 ls
ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints,linestyle='dotted')
plt.show()

#使用简写
plt.plot(ypoints, ls = '-.')
plt.show()

#线的颜色可以使用 color 参数来定义，简写为 c
ypoints = np.array([6, 2, 13, 10])

plt.plot(ypoints, color = 'r')
plt.show()

#使用简写
plt.plot(ypoints,c='#8FBC8F')
plt.show()

#线的宽度可以使用 linewidth 参数来定义，简写为 lw，值可以是浮点数
plt.plot(ypoints, linewidth = '12.5')
plt.show()

#使用简写
plt.plot(ypoints,lw='3.3')
plt.show()

#plot() 方法中可以包含多对 x,y 值来绘制多条线
y1 = np.array([3, 7, 5, 9])
y2 = np.array([6, 2, 13, 10])

plt.plot(y1)
plt.plot(y2)
plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 7, 5, 9])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 13, 10])
plt.plot(x1, y1, x2, y2)
plt.show()