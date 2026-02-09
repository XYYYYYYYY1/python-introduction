import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
#Matplotlib imshow() 方法
#显示灰度图像
img = np.random.rand(10, 10)

plt.imshow(img,cmap='gray')
plt.show()

#显示彩色图像
img = np.random.rand(10, 10, 3)

plt.imshow(img)
plt.show()

#显示热力图
img = np.random.rand(10, 10)

plt.imshow(img,cmap='hot')
plt.show()

#显示地图
img = Image.open('map.jpeg')
data=np.array(img)
plt.imshow(data)
plt.axis('off')
plt.show()

#显示矩阵
data = np.random.rand(10, 10)

plt.imshow(data)

plt.show()