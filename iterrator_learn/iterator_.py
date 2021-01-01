from collections.abc import Iterable, Iterator

# print(isinstance([1,2,3], Iterable))
# print(isinstance(range(10), Iterable))

class Classmate(object):
    def __init__(self):
        self.classmates = list()

    def add_classmate(self, name):
        self.classmates.append(name)

    def __iter__(self):
        return ClassmateIterator(self)


class ClassmateIterator(object):
    def __init__(self, obj):
        self.obj = obj
        self.cur = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.cur < len(self.obj.classmates):
            res = self.obj.classmates[self.cur]
            self.cur += 1
            return res
        else:
            raise StopIteration


classmate = Classmate()
# print(isinstance(classmate, Iterable))
# print(isinstance(iter(classmate), Iterator))
# classmate = iter(classmate)
# print(next(classmate))
classmate.add_classmate("liruonan")
classmate.add_classmate("lixiaokou")
classmate.add_classmate("xiaojun")
classmate.add_classmate("meinan")
classmate.add_classmate("ruonan")

for i in classmate:
    print(i)