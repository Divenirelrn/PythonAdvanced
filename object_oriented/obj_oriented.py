class Parent(object):
    def __init__(self):
        print("----parent------")


class Son1(Parent):
    def __init__(self):
        print("-----son1------")
        # Parent.__init__(self)
        super().__init__()


class Son2(Parent):
    def __init__(self):
        print("-------son2--------")
        # Parent.__init__(self)
        super().__init__()


class Grandson(Son1, Son2):
    def __init__(self):
        print("------grandson-------")
        # Son1.__init__(self)
        # Son2.__init__(self)
        super().__init__()


grandson = Grandson()
print(Grandson.__mro__)