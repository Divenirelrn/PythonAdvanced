class file(object):
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.f = open(self.file_name, self.mode)
        return self.f

    def __exit__(self, *args): #接受位置参数
        self.f.close()

with file("../data/000000000009.jpg", "rb") as fp:
    data = fp.read()

print(data)