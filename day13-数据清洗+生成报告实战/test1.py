# 完整实战示例：使用 Titanic 数据集进行数据清洗和统计分析
# 假设你已从 Kaggle 下载 Titanic 的 train.csv 文件，并放置在当前目录
# 如果没有，访问 https://www.kaggle.com/c/titanic/data 下载 train.csv
import pandas as pd
import numpy as np
#1、读取数据
df=pd.read_csv('train.csv')
print("数据读取成功，形状为：",df.shape)

#2、查看数据概述
print("\n=== 数据信息 ===")
df.info()
print("\n=== 描述性统计 ===")
print(df.describe())

#计算缺失值的比例
missing_ratio=df.isnull().mean()*100
print("\n=== 缺失值比例 (%) ===")
print(missing_ratio[missing_ratio > 0])  # 只显示有缺失的列

#3、处理缺失值
#Age:用中位数填充
df['Age'] = df['Age'].fillna(df['Age'].median())

#Embarked:用众数填充
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

#Cabin:缺失太多（大于70%）直接删除列
df = df.drop('Cabin', axis=1)

print("\n=== 缺失值处理后，剩余缺失 ===")
print(df.isnull().sum())

#4、异常值处理
#Age: 移除不合理值（如 <0 或 >120）
df=df[(df['Age']>=0)&(df['Age']<=120)]

#Fare: 使用 IQR 方法移除极端异常值
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['Fare'] >= lower_bound) & (df['Fare'] <= upper_bound)]
print("\n=== 异常值处理后，形状：", df.shape)

#5、类型转换
#Sex: 类别转数值（male=0, female=1）
df['Sex']=df['Sex'].map({'male':0,'female':1})

#Embarked:one-hot编码
df=pd.get_dummies(df,columns=['Embarked'],prefix='Embarked')
print("\n=== 类型转换后，数据类型 ===")
print(df.dtypes)

#6、新特征工程
#家庭人数:SibSp + Parch + 1（本人）
df['FamilySize']=df['SibSp']+df['Parch']+1

#票价分箱：低/中/高（使用 qcut 等距分箱）
df['FareBin']=pd.qcut(df['Fare'],q=3,labels=['Low', 'Medium', 'High'])

#从姓名提取称呼
df['Title']=df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
df['Title'] = df['Title'].replace(['Lady', 'Countess', 'Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
df['Title'] = df['Title'].replace('Mlle', 'Miss')
df['Title'] = df['Title'].replace('Ms', 'Miss')
df['Title'] = df['Title'].replace('Mme', 'Mrs')

#Title转数值
title_mapping={'Mr': 1, 'Miss': 2, 'Mrs': 3, 'Master': 4, 'Rare': 5}
df['Title']=df['Title'].map(title_mapping).fillna(0)

print("\n=== 新特征示例 ===")
print(df[['FamilySize', 'FareBin', 'Title']].head())

#7、groupby统计
#不同性别/舱位平均票价
avg_fare=df.groupby(['Sex','Pclass'])['Fare'].mean().reset_index()
avg_fare.columns = ['Sex', 'Pclass', 'Avg_Fare']

#不同性别/舱位的生存率
survival_rate=df.groupby(['Sex','Pclass'])['Survived'].mean().reset_index()
survival_rate.columns = ['Sex', 'Pclass', 'Survival_Rate']
survival_rate['Survival_Rate'] *= 100

#合并统计
stats=pd.merge(avg_fare,survival_rate, on=['Sex', 'Pclass'])

print("\n=== Groupby 统计结果 ===")
print(stats)

#8、把所有统计结果写入 txt 文件
#使用 contextlib redirect_stdout（更高级，捕获所有 print）
from contextlib import redirect_stdout
with open('report.txt','w',encoding='utf-8') as f:
    with redirect_stdout(f):
        print("=== 数据基本统计 ===\n")
        print(df.describe().to_string() + "\n\n")
        print("=== Groupby 统计 ===\n")
        print(stats.to_string() + "\n\n")
        print("=== 缺失值比例 (%) ===\n")
        print(missing_ratio[missing_ratio > 0].to_string() + "\n\n")
        print("=== 新特征头5行 ===\n")
        print(df[['FamilySize', 'FareBin', 'Title']].head().to_string() + "\n\n")
        print("=== 完整数据头5行 ===\n")
        print(df.head().to_string() + "\n\n")
        print("=== 结束报告 ===\n")

print("\n报告已写入 report.txt 文件")
