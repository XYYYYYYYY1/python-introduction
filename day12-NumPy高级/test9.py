import numpy as np
#字节交换
#numpy.ndarray.byteswap() 函数将 ndarray 中每个元素中的字节进行大小端转换
a = np.array([1,  256,  8755], dtype = np.int16)
print(a)
print(map(hex,a))
print(a.byteswap(True))
print(map(hex,a))