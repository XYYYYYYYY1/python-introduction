#lambda匿名函数
#无参数
f=lambda : "Hello World"
print(f())

#有单个参数
x=lambda a:a+10
print(x(5))

#有多个参数
y=lambda a,b:a*b
print(y(3,6))

z=lambda a,b,c:a+b+c
print(z(2,3,4))

#lambda与map()
list1=[1,2,3,4,5]
squared=list(map(lambda x:x**2,list1))
print(squared)

#lambda与reduce()
from functools import reduce
product=reduce(lambda x,y:x*y,list1)
print(product)