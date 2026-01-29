import matplotlib.pyplot as plt
import numpy as np
#Matplotlib imsave() 方法
img_data = np.random.random((100, 100))
plt.imshow(img_data)
plt.imsave('test.png',img_data)