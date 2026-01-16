#方法重写
class Parent:
    def method(self):
        print("parent")

class Child(Parent):
    def method(self):
        print("child")

c=Child()
#子类调用重写方法
c.method()
#用子类对象调用父类已被覆盖的方法
super(Child,c).method()