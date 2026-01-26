#部分Series方法
import pandas as pd
data=[1,2,3,4,5,6]
index=['a','b','c','d','e','f']
s=pd.Series(data,index=index)
#查看基本信息
print("索引：",s.index)
print("数据：",s.values)
print("数据类型：",s.dtype)
print("前两行数据：",s.head(2))
#使用map函数将每个元素加倍
s_doubled=s.map(lambda x:x*2)
print("元素加倍后：",s_doubled)
#计算累计和
s_sum=s.cumsum()
print("累计求和：", s_sum)
#排序
s_sorted=s.sort_values()
print("排序后的Series：",s_sorted)