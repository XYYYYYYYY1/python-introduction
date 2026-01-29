import matplotlib.pyplot as plt
import numpy as np
#Matplotlib imread() 方法
img=plt.imread('map.jpeg')
plt.imshow(img)
plt.show()

#通过更改 numpy 数组来修改图像
img_array=plt.imread('tiger.jpeg')
tiger=img_array/255

# 显示图像
plt.figure(figsize=(10,6))

for i in range(1,5):
    plt.subplot(2,2,i)
    x = 1 - 0.2 * (i - 1)
    plt.axis('off')
    plt.title('x={:.1f}'.format(x))
    plt.imshow(tiger*x)

plt.show()

#裁剪图像
plt.figure(figsize=(6,6))
plt.imshow(tiger[:300,100:400,:])
plt.axis('off')
plt.show()

#将 RGB 颜色的绿色和蓝色坐标的数组元素设置为 0
red_tiger = tiger.copy()

red_tiger[:, :,[1,2]] = 0

plt.figure(figsize=(10,10))
plt.imshow(red_tiger)
plt.axis('off')
plt.show()