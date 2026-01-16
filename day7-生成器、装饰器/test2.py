#迭代器的创建
#StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。
class MyNumber:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a<=5:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration

myclass=MyNumber()
it=iter(myclass)
for i in it:
    print(i)