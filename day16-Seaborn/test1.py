import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#Seaborn 教程
#安装 Seaborn   pip install seaborn
#示例
sns.set_theme(style='darkgrid',palette='pastel')

products=["Product A", "Product B", "Product C", "Product D"]
sales=[120, 210, 150, 180]

sns.barplot(x=products,y=sales)

plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales by Category")

plt.show()

#散点图 - sns.scatterplot()
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df=pd.DataFrame(data)

sns.scatterplot(x='A',y='B',data=df)
plt.show()

#折线图 - sns.lineplot()
sns.lineplot(x='A',y='B',data=df)
plt.show()

#柱状图 - sns.barplot()
data = {'Category': ['A', 'B', 'C'], 'Value': [3, 7, 5]}
df = pd.DataFrame(data)

sns.barplot(x='Category',y='Value',data=df)
plt.show()

#箱线图 - sns.boxplot()
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'], 'Value': [3, 7, 5, 9, 2, 6]}
df = pd.DataFrame(data)

sns.boxplot(x='Category',y='Value',data=df)
plt.show()

#热图 - sns.heatmap()
data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)

# 创建一个相关性矩阵
correlation_matrix=df.corr()

sns.heatmap(correlation_matrix,annot=True,cmap='coolwarm',fmt='.2f')
plt.show()

#小提琴图 - sns.violinplot()
data = {'Category': ['A', 'A', 'B', 'B', 'C', 'C'], 'Value': [3, 7, 5, 9, 2, 6]}
df = pd.DataFrame(data)

sns.violinplot(x='Category', y='Value', data=df)
plt.show()