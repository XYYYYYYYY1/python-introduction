from matplotlib import pyplot as plt
import matplotlib
import numpy as np
#Matplotlib 轴标签和标题
#使用 xlabel() 和 ylabel() 方法来设置 x 轴和 y 轴的标签
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x, y)

plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()

#使用 title() 方法来设置标题
x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x, y)

plt.title("test")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.show()

#图形中文显示
zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf")

x=np.arange(1,11)
y=2*x+5
# fontproperties 设置中文显示，fontsize 设置字体大小
plt.title("菜鸟教程 - 测试", fontproperties=zhfont1)
plt.xlabel("x轴",fontproperties=zhfont1)
plt.ylabel("y轴",fontproperties=zhfont1)
plt.plot(x,y)
plt.show()

#自定义字体的样式
'''
title() 方法提供了 loc 参数来设置标题显示的位置，可以设置为: 'left', 'right', 和 'center'， 默认值为 'center'。

xlabel() 方法提供了 loc 参数来设置 x 轴显示的位置，可以设置为: 'left', 'right', 和 'center'， 默认值为 'center'。

ylabel() 方法提供了 loc 参数来设置 y 轴显示的位置，可以设置为: 'bottom', 'top', 和 'center'， 默认值为 'center'。
'''
zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf",size=18)
font1 = {'color':'blue','size':20}
font2 = {'color':'darkred','size':15}
x=np.arange(1,11)
y=2*x+5
plt.title("菜鸟教程 - 测试", fontproperties=zhfont1,fontdict=font1,loc="left")
plt.xlabel("x 轴", fontproperties=zhfont1,loc="left")
plt.ylabel("y 轴", fontproperties=zhfont1,loc="top")
plt.plot(x,y)
plt.show()
