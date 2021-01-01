class Foo(object):
    livehood = "guangzhou" #一般通过类名调用

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__birth = "0422"

    @property
    def now_age(self):
        new_age = self.age + 6
        return new_age

    @now_age.setter
    def now_age(self, value):
        self.age = value

    @now_age.deleter
    def now_age(self):
        del self.age #del方法 -> list, dict, obj(list与dict也是obj)

    def get_birth(self):
        return self.__birth

    def set_birth(self, value):
        self.__birth += value

    def del_birth(self):
        del self.__birth

    BIRTH = property(get_birth, set_birth, del_birth)

    def say_name(self):
        print(self.name)

    #类方法将类作为参数进行操作，进行类相关的操作
    @classmethod
    def say_place(cls):
        print(cls.livehood)

    @staticmethod
    def say_hello():
        print("hello")


foo = Foo("xiaojun", 18)
print(foo.age)
foo.say_name()
foo.say_place()
foo.say_hello()
print(foo.now_age)
foo.now_age = 20
print(foo.now_age)
del foo.now_age
# print(foo.now_age)
print(foo.BIRTH)
foo.BIRTH = "20"
print(foo.BIRTH)