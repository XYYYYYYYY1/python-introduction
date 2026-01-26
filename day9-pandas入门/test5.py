import pandas as pd
#读取csv文件
df=pd.read_csv('output.csv')
print(df)

#写入csv文件
name=['Google','Baidu','Wiki']
site=['www.google.com','www.baidu.com','www.wiki.com']
age=[10,12,13]
dict={'name':name,'site':site,'age':age}
df=pd.DataFrame(dict)
df.to_csv('site.csv')

#数据处理  head()
df=pd.read_csv('site.csv')
print(df.head())
print(df.head(2))

#tail()
print(df.tail())
print(df.tail(2))