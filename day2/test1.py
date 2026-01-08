#列表
list1=['mww','wxy','xwh']
list2=[1,2,3,4]

#列表访问与字符串相似
print(list1)
print(list1[2])
print(list1[0:2])
print(list1[-2])

#修改列表
print()
list2[2]=5
print(list2)
list1.append('zzh')
print(list1)

#删除列表元素
print()
del list1[3]
print(list1)

#列表拼接
print()
list3=[1,2,3,4]
list3+=[5,6]
print(list3)
list4=[5,6,7,8]
print(list3+list4)

#列表嵌套
print()
list5=[[1,2,3],[4,5,6]]
print(list5)
print(list5[-1])

#列表函数
print()
list6=[1,2,3,4,5,6]
print(list6)
print(len(list6))
print(max(list6))
