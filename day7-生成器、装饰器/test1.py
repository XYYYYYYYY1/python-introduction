import sys
#迭代器
list=[1,2,3,4]
it=iter(list)
print(it)
print(next(it))
next(it)
print(next(it))

#遍历迭代器对象
print()
list2=[1,2,3,4]
it=iter(list2)   #创建迭代器对象
for i in it:
    print(i,end=" ")
print()

list3=[1,2,3,4]
it=iter(list3)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()