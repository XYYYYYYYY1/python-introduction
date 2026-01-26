#多重索引
import pandas as pd
#创建多重索引 方法1
index_tuples = [('A', 1), ('A', 2), ('B', 1), ('B', 2)]
multi_index=pd.MultiIndex.from_tuples(index_tuples,names=['Letter','Number'])
df=pd.DataFrame({'Value': [10, 20, 30, 40]},index=multi_index)
print(multi_index)
print(df)

#方法2
print()
index_values = [['A', 'B'], [1, 2]]
multi_index=pd.MultiIndex.from_product(index_values,names=['Letter','Number'])
df=pd.DataFrame({'Value': [10, 20, 30, 40]},index=multi_index)
print(multi_index)
print(df)

#方法3
print()
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
df.set_index(['Letter', 'Number'], inplace=True)
print(df)

#访问多重索引数据
print()
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)
df.set_index(['Letter', 'Number'], inplace=True)
#使用 loc[] 选择数据
print(df.loc['A',1])
#使用 xs() 获取交叉数据
print(df.xs(1, level='Number'))

#排序多重索引
print()
df_sorted = df.sort_index(level=['Letter', 'Number'], ascending=[True, False])
print(df_sorted)

#聚合操作
df_grouped = df.groupby(['Letter', 'Number']).sum()
print(df_grouped)

#重设索引
df_reset=df.reset_index()
print(df_reset)

#多重索引的缺失值
print()
data = {
    'Letter': ['A', 'A', 'B', 'B'],
    'Number': [1, 2, 1, 2],
    'Value': [10, None, 30, 40]
}
df = pd.DataFrame(data)
df.set_index(['Letter', 'Number'], inplace=True)
df_filled = df.fillna(0)
print(df_filled)