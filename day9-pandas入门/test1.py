#使用 pip 安装 pandas
#简单的pandas示例
import pandas as pd
my_dataset={
    'sites':['Google','Wiki','Baidu'],
    'number':['1','2','3']
}
my_var=pd.DataFrame(my_dataset)
print(my_dataset)
print(my_dataset['sites'])
print(my_var)
