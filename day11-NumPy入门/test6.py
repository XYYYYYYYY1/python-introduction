import numpy as np
#广播Broadcast
a = np.array([1,2,3,4])
b = np.array([10,20,30,40])
c = a * b
print (c)

a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = np.array([0,1,2])
bb=np.tile(b,(4,1))
print(a + b)
print(a+bb)
