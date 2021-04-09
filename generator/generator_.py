#列表生成器方式make一个生成器
g = (x * x for x in range(10))

#yield方式
import time

def worker1():
    while True:
        print("----------worker1---------------")
        time.sleep(0.5)
        yield


def worker2():
    while True:
        print("----------worker2---------------")
        time.sleep(0.5)
        yield


def main():
    w1 = worker1()
    w2 = worker2()
    while True:
        next(w1)
        next(w2)


if __name__ == "__main__":
    main()