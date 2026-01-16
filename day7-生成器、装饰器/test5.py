#装饰器示例
def dec(func):
    def wrapper():
        print("函数执行前：")
        func()
        print("函数执行完成")
    return wrapper

@dec
def say():
    print("hello")

say()

