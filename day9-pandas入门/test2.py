#Series示例
import pandas as pd
series=pd.Series([1,2,3,4],name='A')
print(series)
#显示设置索引
custom_index=[1,2,3,4]
series_with_index=pd.Series([1,2,3,4],index=custom_index,name='A')
print(series_with_index)

#创建Series
a=[1,2,3]
my_var=pd.Series(a)
print(my_var)
print(my_var[1])

b=['Google','Wiki','Baidu']
my_var2=pd.Series(b,index=['x','y','z'])
print(my_var2)
print(my_var2['x'])

#类似字典创建Series
sites = {1: "Google", 2: "Wiki", 3: "Baidu"}
myvar = pd.Series(sites, index = [1, 2],name='test')
print(myvar)
