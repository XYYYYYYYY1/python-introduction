#使用yield实现斐波那契数列
import sys
def f(n):
    a,b,c=1,1,1
    while True:
        if c>n:
            return
        yield a
        a,b=b,a+b
        c+=1
# f 是一个迭代器，由生成器返回生成
f=f(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
