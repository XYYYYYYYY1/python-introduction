#JSON
import pandas as pd
#从JSON文件加载数据
df=pd.read_json('sites.json')
print(df.to_string())

data=[
   {
   "id": "A001",
   "name": "菜鸟教程",
   "url": "www.runoob.com",
   "likes": 61
   },
   {
   "id": "A002",
   "name": "Google",
   "url": "www.google.com",
   "likes": 124
   },
   {
   "id": "A003",
   "name": "淘宝",
   "url": "www.taobao.com",
   "likes": 45
   }
]
df = pd.DataFrame(data)
print(df)

# 字典格式的JSON
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}
# 读取 JSON 转为 DataFrame
df = pd.DataFrame(s)
print(df)

#从URL中读取JSON数据
URL = 'https://static.jyshare.com/download/sites.json'
df = pd.read_json(URL)
print(df)

#从 JSON 字符串加载数据
# JSON 字符串
json_data = '''
[
  {"Name": "Alice", "Age": 25, "City": "New York"},
  {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
  {"Name": "Charlie", "Age": 35, "City": "Chicago"}
]
'''
# 从 JSON 字符串读取数据，指定 orient='records' Pandas 未来版本将不再支持直接将 JSON 字符串字面量传递给 pd.read_json()方法。需要将其包装在 StringIO对象中。
df = pd.read_json(json_data, orient='records')
print(df)

#内嵌的JSON数据 nested_list.json
print()
df = pd.read_json('nested_list.json')
print(df)

#json_normalize() 方法将内嵌的数据完整的解析
print()
import json
# 使用 Python JSON 模块载入数据
with open('nested_list.json','r') as f:
    data=json.loads(f.read())
# 展平数据
#record_path设置为 ['students'] 用于展开内嵌的 JSON 数据 students  meta 参数来显示class,school_name
df_nested_list = pd.json_normalize(
    data,
    record_path =['students'],
    meta=['school_name', 'class']
)
print(df_nested_list)

#读取内嵌数据中的一组数据
#使用到 glom 模块来处理数据套嵌，glom 模块允许我们使用.来访问内嵌对象的属性
#第一次使用需要pip3 install glom
print()
from glom import glom
df=pd.read_json('nested_deep.json')
data=df['students'].apply(lambda row: glom(row, 'grade.math'))
print(data)

#将 DataFrame 转换为 JSON
print()
# 创建 DataFrame
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
})
# 将 DataFrame 转换为 JSON 字符串
json_str=df.to_json()
print(json_str)
# 将 DataFrame 转换为 JSON 文件，指定 orient='records'
df.to_json('data.json', orient='records', lines=True)

# 创建 DataFrame，包含日期数据
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Date': pd.to_datetime(['2021-01-01', '2022-02-01', '2023-03-01']),
    'Age': [25, 30, 35]
})
# 将 DataFrame 转换为 JSON，并指定日期格式为 'iso'
json_str = df.to_json(date_format='iso')
print(json_str)