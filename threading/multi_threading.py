import threading
import time


num = 0


def add_one(lock):
    global num
    for i in range(10):
        lock.acquire()
        num += 1
        lock.release()
        time.sleep(0.5)
        print("add_one", num)


def sub_one(lock):
    global num
    for i in range(10):
        lock.acquire()
        num -= 1
        lock.release()
        time.sleep(1)
        print("sub_one:", num)


def main():
    lock = threading.Lock()
    t1 = threading.Thread(target=add_one, args=(lock,))
    t2 = threading.Thread(target=sub_one, args=(lock,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == "__main__":
    main()