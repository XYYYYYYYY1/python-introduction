import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#Matplotlib 直方图
#hist() 方法是 Matplotlib 库中的 pyplot 子库中的一种用于绘制直方图的函数
data = np.random.randn(1000)
plt.hist(data,bins=30,color='skyblue',alpha=0.8)
plt.title('hist() test')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()

# hist() 函数绘制多个数据组的直方图
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(2, 1, 1000)
data3 = np.random.normal(-2, 1, 1000)

plt.hist(data1,bins=30,label='Data 1',alpha=0.5)
plt.hist(data2,bins=30,label='Data 2',alpha=0.5)
plt.hist(data3,bins=30,label='Data 3',alpha=0.5)

plt.title('hist() TEST')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

plt.show()

#结合Pandas
random_data = np.random.normal(170, 10, 250)
dataframe = pd.DataFrame(random_data)
dataframe.hist()

plt.title('hist() Test')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')

plt.show()

#使用 Pandas 中的 Series 对象绘制直方图
data=pd.Series(np.random.normal(size=100))
plt.hist(data, bins=10)

plt.title('hist() Test')
plt.xlabel('X-Value')
plt.ylabel('Y-Value')

plt.show()