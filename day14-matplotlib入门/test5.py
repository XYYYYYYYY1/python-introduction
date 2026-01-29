import matplotlib.pyplot as plt
import numpy as np
#Matplotlib 网格线
#使用 pyplot 中的 grid() 方法来设置图表中的网格线
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])


plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)
#axis 参数使用 x，设置 x 轴方向显示网格线
plt.grid(axis='x')

plt.show()

x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])


plt.title("RUNOOB grid() Test")
plt.xlabel("x - label")
plt.ylabel("y - label")

plt.plot(x, y)

plt.grid(color='r',linestyle='--',lw=0.5)

plt.show()
