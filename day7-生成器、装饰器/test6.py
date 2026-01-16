#带参数的装饰器
def dec(func):
    def wrapper(*args,**kwargs):
        print("函数执行前：")
        func(*args,**kwargs)
        print("函数执行完成")
    return wrapper

@dec
def greet(name):
    print("hello",name)

greet("mww")

#带参数的装饰器,需要额外定义一个外层函数
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num_times):
                print(i)
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()