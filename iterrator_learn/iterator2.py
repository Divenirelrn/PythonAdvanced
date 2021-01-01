
class Classmate(object):
    def __init__(self):
        self.classmates = list()
        self.cur = 0
        
    def add_name(self, name):
        self.classmates.append(name)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.cur < len(self.classmates):
            res = self.classmates[self.cur]
            self.cur += 1
            return res
        else:
            raise StopIteration
        
classmate = Classmate()
classmate.add_name("liruonan")
classmate.add_name("lixiaokou")
classmate.add_name("xiaojun")
classmate.add_name("meinan")
classmate.add_name("ruonan")
for i in classmate:
    print(i)