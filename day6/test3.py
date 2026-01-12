#类定义
class people:
    #定义基本属性
    name=''
    age=0
    #定义私有属性，私有属性在类外部无法直接访问
    __weight=0
    #定义构造方法
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s说：我%d岁" %(self.name,self.age))

p=people('mww',21,160)
p.speak()

#单继承示例
class student(people):
    grade=0
    def __init__(self,n,a,w,g):
        #调用父类的构造函数
        people.__init__(self,n,a,w)
        self.grade=g
    #覆写父类方法
    def speak(self):
        print("%s说：我%d岁，在读%d年级" %(self.name,self.age,self.grade))

s=student('zbh',12,100,6)
s.speak()

#另一个类定义
class speaker():
    topic=''
    name=''
    def __init__(self,t,n):
        self.topic=t
        self.name=n
    def speak(self):
        print("我叫%s,我演说的主题是%s"%(self.name,self.topic))

#多继承示例
class sample(speaker,student):
    a=''
    def __init__(self,n,a,w,g,t):
        speaker.__init__(self,t,n)
        student.__init__(self,n,a,w,g)

t=sample("mww",22,150,4,"Java")
#方法名同，默认调用的是在括号中参数位置排前父类的方法
t.speak()
