
#通用装饰器
def w(func):
    def inner(*args, **kwargs):
        print("---------验证一-------------")
        print("---------验证二-------------")
        return func(*args, **kwargs)
    return inner


@w
def f1():
    print("-------I am f1-----------")

@w
def f2():
    print("-------I am f2------------")


@w
def f3(num):
    print("--------I am f3: %d---------" % num)


@w
def f4():
    return "hello"


f1()
f2()
f3(5)
print(f4())


#多个装饰器对同一个函数进行装饰
def dec1(func):
    def inner():
        print("--------权限一-----------")
        print("--------权限二-----------")
        func()
    return inner


def dec2(func):
    def inner():
        print("--------权限三-----------")
        print("--------权限四-----------")
        func()
    return inner


@dec1
@dec2
def test():
    print("-----test---------")


test()


#用类作为装饰器
class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("---------权限一---------")
        print("---------权限二---------")
        return self.func(*args, **kwargs)


@Test
def test1(word):
    return "----------test1: %s-------" % word


print(test1("nihao"))


#带参数的装饰器
def set_level(level):
    def set_authority(func):
        def inner():
            if level == 1:
                print("-------权限一---------")
            elif level == 2:
                print("--------权限二---------")
            func()
        return inner
    return set_authority


@set_level(1)
def test2():
    print("-----test2-------")


@set_level(2)
def test3():
    print("------test3------")


test2()
test3()