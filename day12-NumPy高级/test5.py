import numpy as np
#数学函数
#三角函数
a = np.array([0,30,45,60,90])
print(np.sin(a*np.pi/180))
print(np.cos(a*np.pi/180))
print(np.tan(a*np.pi/180))
#numpy.around() 函数返回指定数字的四舍五入值
a = np.array([1.0,5.55,  123,  0.567,  25.532])
print(np.around(a))
print(np.around(a, decimals =  1))
print(np.around(a, decimals =  -1))
#numpy.floor() 返回小于或者等于指定表达式的最大整数，即向下取整
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(a)
print(np.floor(a))
#numpy.ceil() 返回大于或者等于指定表达式的最小整数，即向上取整
a = np.array([-1.7,  1.5,  -0.2,  0.6,  10])
print(a)
print(np.ceil(a))