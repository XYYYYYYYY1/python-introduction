#类实例
class MyClass:
    i=12345
    def f(self):
        return "hello world"

#实例化类
x=MyClass()

#访问类和类的方法
print("属性i的值为：",x.i)
print("方法输出为：",x.f())

