#相关性分析
#使用 corr() 方法计算数据框中各列之间的 Pearson 相关系数
import pandas as pd
data = {
    'Height': [150, 160, 170, 180, 190],
    'Weight': [45, 55, 65, 75, 85],
    'Age': [20, 25, 30, 35, 40]
}
df=pd.DataFrame(data)
correlation=df.corr(method='pearson')
print(correlation)

#计算斯皮尔曼等级相关系数
spearman_correlation = df.corr(method='spearman')
print(spearman_correlation)

#计算肯德尔秩相关系数
kendall_correlation = df.corr(method='kendall')
print(kendall_correlation)