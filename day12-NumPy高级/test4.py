import numpy as np
#字符串函数
#numpy.char.add() 函数依次对两个数组的元素进行字符串连接
print(np.char.add(['hello'],[' mww']))
#numpy.char.multiply() 函数执行多重连接
print(np.char.multiply('mww ',3))
#numpy.char.center() 函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充
print(np.char.center('mww',20,fillchar='*'))
#numpy.char.capitalize() 函数将字符串的第一个字母转换为大写
print(np.char.capitalize('mww'))
#numpy.char.lower() 函数对数组的每个元素转换为小写
print(np.char.lower(['RUNOOB','GOOGLE']))
#numpy.char.upper() 函数对数组的每个元素转换为大写
print (np.char.upper(['runoob','google']))
#numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组
# 分隔符默认为空格
print (np.char.split ('i like runoob?'))
# 分隔符为 .
print (np.char.split ('www.runoob.com', sep = '.'))
#numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组
print (np.char.splitlines('i\nlike runoob?'))
print (np.char.splitlines('i\rlike runoob?'))
#numpy.char.strip() 函数用于移除开头或结尾处的特定字符
print(np.char.strip(['arunooba','admin','java'],'a'))
#numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
print(np.char.join([':','-'],['mwwww','google']))
#numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串
print (np.char.replace ('i like runoob', 'oo', 'cc'))
#numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数
a = np.char.encode('runoob', 'cp500')
print (a)
print (np.char.decode(a,'cp500'))