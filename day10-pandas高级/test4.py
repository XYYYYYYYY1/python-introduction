#数据合并与连接
import pandas as pd
#merge()  数据库风格连接
left = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie']})
right = pd.DataFrame({'ID': [1, 2, 4], 'Age': [24, 27, 22]})
result=pd.merge(left,right,on='ID',how='inner')
print(result)

#concat()  沿轴连接
print()
df1 = pd.DataFrame({'A': [1, 2, 3]})
df2 = pd.DataFrame({'A': [4, 5, 6]})
result=pd.concat([df1,df2],axis=0,ignore_index=True)
print(result)

#join()  基于索引连接
print()
left = pd.DataFrame({'A': [1, 2, 3]}, index=[1, 2, 3])
right = pd.DataFrame({'B': [4, 5, 6]}, index=[1, 2, 4])
result=left.join(right,how='inner')
print(result)

#透视表
print()
data = {'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
        'Category': ['A', 'B', 'A', 'B'],
        'Sales': [100, 150, 200, 250]}
df = pd.DataFrame(data)
pivot_table=pd.pivot_table(df,values='Sales',index='Date',columns='Category',aggfunc='sum',fill_value=0)
print(pivot_table)

#交叉表
print()
data = {'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Region': ['North', 'South', 'North', 'South', 'West', 'East']}
df = pd.DataFrame(data)
cross_table=pd.crosstab(df['Category'],df['Region'])
print(cross_table)

#自定义函数
#apply() — 应用函数到 DataFrame 或 Series 上
print()
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [10, 20, 30, 40]})
def custom_func(x):
        return x*2
df['A']=df['A'].apply(custom_func)
print(df)

#map() — 1、在整个 DataFrame 上应用函数 2、 应用函数到 Series 上
print()
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df=df.map(lambda x: x**2)
print(df)

#时间序列处理
#date_range() — 生成时间序列
print()
date_range=pd.date_range(start='2026-01-01',periods=5,freq='D')
print(date_range)

#日期和时间的偏移
print()
date=pd.to_datetime('2026-01-01')
new_date=date+pd.Timedelta(days=10)
print(new_date)

#时间窗口操作
print()
df = pd.DataFrame({'Value': [10, 20, 30, 40, 50]})
df['Rolling_Mean']=df['Value'].rolling(window=3).mean()
print(df)