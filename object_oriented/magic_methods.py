
class Foo(object):
    """
        A practice class
    """
    def __init__(self):
        print("-----init-----")

    def say_hello(self):
        print("hello")


foo = Foo()
print(Foo.__doc__)
print(foo.__class__)
print(foo.__module__)
print(foo) #自动调用__call__方法
print(Foo.__dict__)
#__getitem__