
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
class MyData():
    def __init__(self):
        self.nums = [1,2,3,4,5,6,7,8]

    def __getitem__(self, item):
        return self.nums[item]

    def __len__(self):
        return len(self.nums)


mydata = MyData()
print(mydata[1])
print(len(mydata))


#__all__(用于限制模块导入)
#使用from model import *, 此时只能导入resnet18, Resnet, resnet50
__all__ = ['resnet18', 'Resnet', 'resnet50']