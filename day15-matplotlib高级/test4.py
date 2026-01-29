import matplotlib.pyplot as plt
import numpy as np
#Matplotlib 饼图
#使用 pie() 来创建一个饼图
y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

#设置饼图各个扇形的标签与颜色
plt.pie(y,
        labels=['A','B','C','D'],
        colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"] )
plt.title("Pie Test")
plt.show()

#突出显示第二个扇形，并格式化输出百分比
sizes = [15, 30, 45, 10]
labels=['A','B','C','D']
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
# 突出显示第二个扇形
explode = (0, 0.1, 0, 0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors,
        autopct='%1.1f%%',shadow=True,startangle=90)
plt.title("Pie Test")
plt.show()