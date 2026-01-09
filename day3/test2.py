#while语句实例
a=1
while a<10:
    print(a)
    a+=2

#while语句使用else
print()
c=0
while c<5:
    print(c,"小于5")
    c+=2
else:
    print(c,"大于或等于5")

#for语句实例
print()
sites=["Beijing","Nanjing","Xian"]
for site in sites:
    print(site)

#打印字符串中每个字符
print()
str1='khalil'
for s in str1:
    print(s)

#配合range使用
print()
for num in range(1,6):
    print(num)

#break和continue与c中类似 注：break从for或while循环中终止，任何对应的循环else块将不执行。

#pass空语句，是为了保持程序结构的完整性。
for letter in 'hello':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")