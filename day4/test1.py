#函数1
def hello():
    print("hello world\n")

hello()

#函数2
def max(a,b):
    if a>b:
        return a
    else:
        return b

a=4
b=5
print(max(a,b),"\n")

#函数3
def area(w,h):
    return w*h

print(area(3,4))

#不可变对象strings,tuples,和numbers,可变对象list,dict