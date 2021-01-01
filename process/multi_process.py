import multiprocessing as mp
import time


def write_msg(msg, q, lock):
    for i in range(10):
        if q.full():
            continue
        lock.acquire()
        q.put(msg)
        lock.release()
        time.sleep(1)
        print("enter queue", q.qsize())


def read_msg(q, lock):
    for i in range(10):
        if q.empty():
            continue
        lock.acquire()
        msg = q.get()
        lock.release()
        time.sleep(1)
        print("exit queue", msg, q.qsize())


def main():
    q = mp.Queue(10)
    lock = mp.Lock()
    p1 = mp.Process(target=write_msg, args=("hello", q, lock))
    p2 = mp.Process(target=read_msg, args=(q,lock))
    [p.start() for p in [p1, p2]]
    [p.join() for p in [p1, p2]]



if __name__ == "__main__":
    main()
