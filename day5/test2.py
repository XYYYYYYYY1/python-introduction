#文件属性
fo=open("foo.txt","w")
print("文件名:",fo.name)
print("是否已经关闭:",fo.closed)
print("访问模式:",fo.mode)

#write
fo.write( "www.runoob.com!\nVery good site!\n")
fo.close()

#read
fo=open("foo.txt","r+")
str=fo.read()
print(str)

#关闭文件
fo.close()

