#数据排序
import pandas as pd
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'Salary': [50000, 60000, 70000, 80000]}
df=pd.DataFrame(data)
df_sorted=df.sort_values(by='Age',ascending=False)
print(df_sorted)

print()
df_sorted_index=df.sort_index(axis=0)
print(df_sorted_index)

#数据聚合
print()
data = {'Department': ['HR', 'Finance', 'HR', 'IT', 'IT'],
        'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Salary': [50000, 60000, 55000, 70000, 75000]}
df=pd.DataFrame(data)
print(df)
grouped=df.groupby('Department')['Salary'].mean()
print(grouped)

#多重聚合
print()
grouped_multiple=df.groupby('Department').agg({'Salary':['mean','sum']})
print(grouped_multiple)

#分组后的排序
print()
grouped_sorted=df.groupby('Department').apply(lambda x: x.sort_values(by='Salary',ascending=False),include_groups=False)
print(grouped_sorted)

#透视表
print()
pivot_table = df.pivot_table(values='Salary', index='Department', aggfunc='mean')
print(pivot_table)