#数据清洗
import pandas as pd
#isnull()判断单元格是否为空
df=pd.read_csv('property-data.csv')
print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())

#指定空数据类型
print()
missing_values=['n/a','na','--']
df=pd.read_csv('property-data.csv',na_values=missing_values)
print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())

#删除包含空数据的行
print()
df=pd.read_csv('property-data.csv')
new_df=df.dropna()
print(new_df.to_string())

#fillna() 方法来替换一些空字段
print()
df=pd.read_csv('property-data.csv')
df.fillna(12345,inplace=True)
print(df)

#指定某一列替换数据
print()
df=pd.read_csv('property-data.csv')
df['PID']=df['PID'].fillna(12345)
print(df)

#mean(),median(),mode()计算列的均值、中位数、众数
print()
df=pd.read_csv('property-data.csv')
x=df['ST_NUM'].mean()
df['ST_NUM']=df['ST_NUM'].fillna(x)
print(df.to_string())

print()
df=pd.read_csv('property-data.csv')
x=df['ST_NUM'].median()
df['ST_NUM']=df['ST_NUM'].fillna(x)
print(df.to_string())

print()
df=pd.read_csv('property-data.csv')
x=df['ST_NUM'].mode()
df['ST_NUM']=df['ST_NUM'].fillna(x)
print(df.to_string())

#清洗格式错误数据
print()
data = {
  "Date": ['2020/12/01', '2020/12/02' , '20201226'],
  "duration": [50, 40, 45]
}
df=pd.DataFrame(data,index=['day1','day2','day3'])
df['Date']=pd.to_datetime(df['Date'],format='mixed')
print(df.to_string())

#清洗错误数据
print()
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}
df=pd.DataFrame(person)
df.loc[2,'age']=30
print(df.to_string())

#设置条件语句清洗错误数据
print()
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}
df=pd.DataFrame(person)
for x in df.index:
    if df.loc[x,'age']>120:
        df.loc[x,'age']=120
print(df.to_string())

#将age>120的数据删除
print()
person = {
  "name": ['Google', 'Runoob' , 'Taobao'],
  "age": [50, 40, 12345]    # 12345 年龄数据是错误的
}
df=pd.DataFrame(person)
for x in df.index:
    if df.loc[x,'age']>120:
        df.drop(x,inplace=True)
print(df.to_string())

#清理重复数据 如果对应的数据是重复的，duplicated() 会返回 True，否则返回 False
print()
person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}
df=pd.DataFrame(person)
print(df.duplicated())

#使用drop_duplicates()方法删除重复数据
print()
person = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}
df=pd.DataFrame(person)
df.drop_duplicates(inplace = True)
print(df)

#填充缺失值示例
print()
data = {'Name': ['Alice', 'Bob', 'Charlie', None],
        'Age': [25, 30, None, 35],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
df['Age']=df['Age'].fillna(df['Age'].mean())
print(df)

#独热编码
print()
data = {'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}
df = pd.DataFrame(data)
df_encoded=pd.get_dummies(df,columns=['City'])
print(df_encoded)

#标准化
from sklearn.preprocessing import StandardScaler
print()
data = {'Age': [25, 30, 35, 40, 45],
        'Salary': [50000, 60000, 70000, 80000, 90000]}
df = pd.DataFrame(data)
#标准化数据
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
print(df_scaled)