#列表推导式
names=['mww','Bob','Mike','Wendy']
new_names=[name.upper()for name in names if len(name)>3]
print(new_names)

#字典推导式
dic={x:x**2 for x in (2,4,6)}
print(dic)

#集合推导式
a={x for x in "abracbdefabc" if x not in "abc"}
print(a)

#元组推导式
tup=(x for x in range(1,10))
# 返回的是生成器对象
print(tup)
print(tuple(tup))