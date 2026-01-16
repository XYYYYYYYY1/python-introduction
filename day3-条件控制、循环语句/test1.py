#if实例
a=100
if a:
    print(a)

b=0
if b:
    print(b)
else:
    print("b is zero")

c=5
if c>5:
    print(">5")
elif c>3:
    print(">3")
else:
    print("no")

#match实例
a=int(input("请输入一个数字"))
match a:
    case 1:
        print("is 1")
    case 0:
        print("is 0")
    case _:
        print("is not 0 or 1")



