#元组，与列表相似，但元组内元素不可修改
tup1=('mww','wxy','xwh')
tup2=(1,2,3)
tup3="a","b","c"
print(tup3)

#元组访问与列表类似，不可修改元素，但可以进行拼接
tup4=tup1+tup2
print(tup4)

#删除元组
del tup4

#元组运算
print(len(tup2))
print(tup2*4)
print(1 in tup2)


