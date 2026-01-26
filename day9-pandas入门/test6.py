import pandas as pd
#Pandas Excel 文件操作

#读取文件操作
#读取默认的第一个表单
df = pd.read_excel('runoob_pandas_data.xlsx')
print(df)

#自定义列名并跳过前两行
print()
df = pd.read_excel('runoob_pandas_data.xlsx',header=0, names=['A', 'B', 'C'], skiprows=2)
print(df)

#写入文件操作
print()
df = pd.DataFrame({
'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'Los Angeles', 'Chicago']
})
df.to_excel('output.xlsx',sheet_name='Sheet1',index=False)

#写入多个表单，使用 ExcelWriter
with pd.ExcelWriter('output.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    df.to_excel(writer, sheet_name='Sheet2', index=False)

#加载文件
excel_file=pd.ExcelFile('output.xlsx')
# 查看所有表单的名称
print(excel_file.sheet_names)
# 读取指定的表单
df = excel_file.parse('Sheet1')
print(df)
# 关闭文件
excel_file.close()

#ExcelWriter写多个表单
df1=pd.DataFrame([["AAA", "BBB"]], columns=["Spam", "Egg"])
df2=pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])
with pd.ExcelWriter("path_to_file.xlsx") as writer:
    df1.to_excel(writer,sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')