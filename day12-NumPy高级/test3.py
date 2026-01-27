import numpy as np
#位运算
a,b=13,17
print(bin(a),bin(b))
print(np.bitwise_and(a,b))
print(np.bitwise_or(a,b))
print(np.bitwise_xor(a,b))
print ('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
print (np.invert(np.array([13], dtype = np.uint8)))
print ('13 的二进制表示：')
print(np.binary_repr(13,width=8))
print ('将 10 左移两位：')
print(np.left_shift(10,2))
print ('将 10 右移两位：')
print(np.right_shift(10,2))